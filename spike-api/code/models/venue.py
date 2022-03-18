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

    def __init__(self,name,location,photo_id,lng,lat,area_id):
        self.name = name
        self.location = location
        self.photo_id = photo_id
        self.lng = lng
        self.lat = lat
        self.area_id = area_id
    
    def json(self):
        return {'name': self.name, 'location': self.location, 'photo_id': self.photo_id,'lng':self.lng,'lat':self.lat,'reports':[report.json() for report in self.reports.all()]}
        
    @classmethod 
    def find_by_name(cls,name):
       return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    