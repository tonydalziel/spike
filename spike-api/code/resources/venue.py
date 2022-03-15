from flask_restful import Resource, reqparse
from models.venue import VenueModel
class Venue(Resource):

    def get(self,name):

        venue = VenueModel.find_by_name(name)

        if venue:
            return venue.json()
        
        return {'message': f"Venue not found {venue}"},404
        