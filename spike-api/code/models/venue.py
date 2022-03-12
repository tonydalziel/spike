from db import db

class VenueModel(db.Model):

    __tablename__ = 'venues'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(30))
    location = db.Column(db.String(100))
    photo_id = db.Column(db.String(100))
    lng = db.Column(db.String(255))
    lat = db.Column(db.String(255))

    #area id foreign key 
    area_id = db.Column(db.Integer,db.ForeignKey('areas.id'))
    area = db.relationship('AreaModel') 

    reports = db.relationship('ReportModel',lazy='dynamic')

    