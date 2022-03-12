from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    reports = db.relationship('ReportModel',lazy='dynamic')

