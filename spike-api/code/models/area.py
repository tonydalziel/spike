from db import db 

class AreaModel(db.Model):

    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    venues = db.relationship('VenueModel',lazy='dynamic')

    def __init__(self,name):
        self.name = name
    
    def json(self):
        return {'area': self.name, 'venues': [venue.json() for venue in self.venues.all()]}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()