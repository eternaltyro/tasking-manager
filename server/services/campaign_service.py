import re
import time

from cachetools import TTLCache, cached
from typing import List
from flask import current_app
from server.models.postgis.utils import NotFound
from server import create_app, db
from server.models.dtos.campaign_dto import CampaignDTO
# from server.models.postgis.Project_Model import Project
# from server.models.dtos.stats_dto import Pagination
from server.models.postgis.campaign import Campaign
# , campaign_projects, campaign_organisations



class CampaignService:

    @staticmethod
    def get_campaign(campaign_id: int) -> Campaign:
        """ Gets the specified campaign """
        campaign = Campaign.query.get(campaign_id)

        if campaign is None:
            raise NotFound()

        return campaign

    @staticmethod
    def get_campaign_as_dto(campaign_id: int):
        """ Gets the specified campaign """
        campaign = CampaignService.get_campaign(campaign_id)

        return campaign.as_dto()

    @staticmethod
    def create_campaign(campaign_dto: CampaignDTO):
        campaign = Campaign.from_dto(campaign_dto)
        campaign.create()
        return campaign

    @staticmethod
    def update_campaign(campaign_dto: CampaignDTO):
        # campaign = Campaign.from_dto(campaign_dto)
        campaign = Campaign.query.get(campaign_dto.id)
        campaign.update(campaign_dto)
        return campaign

    # @staticmethod
    # def get_all_campaigns():
    #     campaigns = Campaign.query.all()
    #     return campaigns_dto

    # @staticmethod
    # def get_campaign_projects(campaign_id: int) -> campaign_projects:
    #     """ Gets the specified campaign """
    #     campaign_projects = campaign_projects.query.group_by(campaign_id).all()
    #     projects = Projects.query.filter(id in campaign_projects.project_id)
    #     if projects is None:
    #         raise NotFound()

    #     return projects

    # @staticmethod
    # def get_campaign_organisations(campaign_id: int) -> campaign_organisations:
    #     """ Gets the specified campaign """
    #     orgs = campaign_organisations.query.filter(campaign_id=campaign_id)

    #     if orgs is None:
    #         raise NotFound()

    #     # if message.to_user_id != int(user_id):
    #         # raise MessageServiceError(f'User {user_id} attempting to access another users message {message_id}')

    #     return orgs

