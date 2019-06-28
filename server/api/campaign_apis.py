import threading
import json
from flask_restful import Resource, request, current_app
from schematics.exceptions import DataError

from server.models.dtos.campaign_dto import CampaignDTO
# , CampaignProjectDTO, CampaignOrganisationDTO
from server.services.campaign_service import CampaignService
from server.models.postgis.utils import NotFound
from server.models.postgis.campaign import Campaign
from server.services.users.authentication_service import token_auth, tm

class CampaignAPI(Resource):

    def get(self, campaign_id):

        try:
            # campaign_id = request.args.get('campaign_id')
            campaign = CampaignService.get_campaign_as_dto(campaign_id)
            return campaign.to_primitive(), 200
        except NotFound:
            return {"Error": "No campaign found"}, 404
        except Exception as e:
            error_msg = f'Messages GET - unhandled error: {str(e)}'
            current_app.logger.critical(error_msg)
            return {"error": error_msg}, 500


    def patch(self, campaign_id):

        try:
            campaign_dto = CampaignDTO(request.get_json())
            campaign_dto.validate()
        except DataError as e:
            current_app.logger.error(f'error validating request: {str(e)}')
            return str(e), 400

        try:
            campaign = CampaignService.update_campaign(campaign_dto, campaign_id)
            return {campaign_dto.name:"Updated"}, 200
        except NotFound:
            return {"Error": "Campaign not found"}, 404
        except Exception as e:
            error_msg = f'User PATCH - unhandled error: {str(e)}'
            current_app.logger.critical(error_msg)
            return {"error": error_msg}, 500


    def post(self):

        try:
            print (request.is_json)
            print("is_json end")
            print(request.get_json())
            campaign_dto = CampaignDTO(request.get_json())
            campaign_dto.validate()
        except DataError as e:
            current_app.logger.error(f'error validating request: {str(e)}')
            return str(e), 400

        try:
            campaign = CampaignService.create_campaign(campaign_dto)
            return {campaign_dto.name :"created"}, 200
        except Exception as e:
            error_msg = f'User POST - unhandled error: {str(e)}'
            current_app.logger.critical(error_msg)
            return {"error": error_msg}, 500
    
    

