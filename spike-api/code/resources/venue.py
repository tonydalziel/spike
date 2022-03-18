from flask_restful import Resource,reqparse
from models.venue import VenueModel
class Venue(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('location',
        type=str,
        required=True,
        help="Every venue needs a location"
    )
    parser.add_argument('photo_id',
        type=str,
        required=True,
        help="Every venue needs a photo id"
    )
    parser.add_argument('lng',
        type=str,
        required=True,
        help="Every venue needs a lng coordinate"
    )
    parser.add_argument('lat',
        type=str,
        required=True,
        help="Every venue needs a lat coordinate"
    )


    def get(self,name):

        venue = VenueModel.find_by_name(name)

        if venue:
            return venue.json()
        
        return {'message': f"Venue not found {venue}"},404

    def post(self,name):
        
        if VenueModel.find_by_name(name):
            return {"message": "A venue with that name already exists"},400

        data = Venue.parser.parse_args()
        venue = VenueModel(name,data['location'],data['photo_id'],data['lng'],data['lat'],data['area_id']) #FIXME: can i use ** abreviation here
        venue.save_to_db()

        return {"message": "Venue created successfully"}, 201
        