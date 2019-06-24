from schematics import Model
from schematics.types import StringType, IntType
# from schematics.types.compound import ListType, ModelType

# from server.models.dtos.stats_dto import Pagination


class CampaignDTO(Model):
    """ DTO used to define a campaign"""
    id = IntType()
    name = StringType()
    logo = StringType()
    url = StringType()
    description = StringType()
    
# class CampaignProjectsDTO
