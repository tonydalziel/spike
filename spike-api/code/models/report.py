from db import db

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