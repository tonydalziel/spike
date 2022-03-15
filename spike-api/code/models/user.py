from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    reports = db.relationship('ReportModel',lazy='dynamic')

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod 
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()

    @classmethod #we call the User class and we are not using self so we we use cls instead
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()
