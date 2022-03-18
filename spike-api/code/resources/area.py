from flask_restful import Resource, reqparse
from models.area import AreaModel


class Area(Resource):

    def get(self,name):

        area = AreaModel.find_by_name(name)

        if area:
            return area.json()
        
        return {'message': f"Area not found {area}"},404
    
    def post(self,name):

        if AreaModel.find_by_name(name):
            return {"message": "An area with that name already exists"},400

        area = AreaModel(name)
        area.save_to_db()

        return {"message": "Area created successfully"}, 201


    