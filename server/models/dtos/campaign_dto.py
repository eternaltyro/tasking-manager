from schematics import Model
from schematics.types import StringType, IntType
# from schematics.types.compound import ListType, ModelType

# from server.models.dtos.stats_dto import Pagination


class CampaignDTO(Model):
    """ DTO used to define a campaign"""
    id = IntType(serialized_name='campaignId')
    name = StringType(required=True)
    logo = StringType(required=False, serialize_when_none=False)
    url = StringType(required=False, serialize_when_none=False)
    description = StringType(required=False, serialize_when_none=False)
    
 