from flask_restful import Resource, reqparse
from models.report import ReportModel
class Report(Resource):

    def get(self,_id):

        report = ReportModel.find_by_id(_id)

        if report:
            return report.json()
        
        return {'message': f"Report not found {report}"},404