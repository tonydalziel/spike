from flask_restful import Resource, reqparse
from models.area import AreaModel


class Area(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="Every area needs a valid name"
    )
    parser.add_argument('id',
        type=int,
        required=True,
        help="Every area needs a valid id"
    )

    def get(self,name):

        area = AreaModel.find_by_name(name)

        if area:
            return area.json()
        
        return {'message': f"Area not found {area}"},404
    