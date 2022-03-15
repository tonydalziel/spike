from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):

    def get(self,email):

        user = UserModel.find_by_email(email)

        if user:
            return user.json()
        
        return {'message': f"User not found {user}"},404