from server import db
# from server.models.postgis.Project_Model import Project
# from server.models.postgis.Organisation_Model import Organisation
from server.models.postgis.user import User
from server.models.dtos.campaign_dto import CampaignDTO

# campaign_projects = db.Table(
#     'campaign_projects', db.metadata,
#     db.Column('campaign_id', db.Integer, db.ForeignKey('campaign.id'), nullable=False),
#     db.Column('project_id', db.Integer, db.ForeignKey('project.id'), nullable=False)
# )

# campaign_organisations = db.Table(
#     'campaign_organisations', db.metadata,
#     db.Column('campaign_id', db.Integer,  db.ForeignKey('campaign.id'), nullable=False),
#     db.Column('organisation_id', db.Integer, db.ForeignKey('organisation.id'), nullable=False)
# )

# campaign_users = db.Table(
#     'campaign_users', db.metadata,
#     db.Column('campaign_id', db.Integer,  db.ForeignKey('campaign.id'), nullable=False),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
# )

class Campaign(db.Model):
    """ Describes an Campaign"""
    __tablename__ = 'campaign'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    logo = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.String)
    
    # projects = db.relationship(
    #     Project,
    #     secondary=campaign_projects,
    #     backref='campaign' 
    # )

    # organisation = db.relationship(
    #     Organisation,
    #     secondary=campaign_organisations,
    #     backref='campaign'
    # )

    # user_campaign = db.relationship(
    #     User,
    #     secondary=campaign_users,
    #     backref='campaign'
    # )

    def create(self):
        """ Creates and saves the current model to the DB """
        db.session.add(self)
        db.session.commit()
    
    def save(self):
        db.session.commit()

    def update(self, dto: CampaignDTO):
        """ Update the user details """
        self.name = dto.name if dto.name else self.name
        self.logo = dto.logo if dto.logo else self.logo
        self.url = dto.url if dto.url else self.url
        self.description = dto.description if dto.description else self.description
        db.session.commit()

    @classmethod
    def from_dto(cls, dto: CampaignDTO):
        """ Creates new message from DTO """
        campaign = cls()
        campaign.url = dto.url
        campaign.name = dto.name
        campaign.logo = dto.logo
        campaign.description = dto.description
        
        
        return campaign

    def as_dto(self)-> CampaignDTO:
        """ Creates new message from DTO """
        campaign_dto = CampaignDTO()
        campaign_dto.id = self.id
        campaign_dto.url = self.url
        campaign_dto.name = self.name
        campaign_dto.logo = self.logo
        campaign_dto.description = self.description
        
        return campaign_dto

    



