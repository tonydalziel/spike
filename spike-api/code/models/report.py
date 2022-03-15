
from db import db
from datetime import datetime

class ReportModel(db.Model):

    __tablename__ = 'reports'
    id = db.Column(db.Integer,primary_key = True)
    time = db.Column(db.Time) #report time; uses datetime.time() struct

    #user id foreign key - get last report by user
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = db.relationship('UserModel') 

    #venue id foreign key - get all reports at venue
    venue_id = db.Column(db.Integer,db.ForeignKey('venues.id'))
    venue = db.relationship('VenueModel') 


    def __init__(self,user_id,venue_id):
        self.user_id = user_id
        self.venue_id = venue_id
        self.time = datetime.time() #NOTE report time corrosponds to when obj is created not when object is saved to db

    def json(self):
        return {'time': self.time}

    #Finds a report that has a unique report id NOTE this is not related to venue id or user id 
    @classmethod 
    def find_by_id(cls,_id):
       return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        