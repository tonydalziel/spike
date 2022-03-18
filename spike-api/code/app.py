from flask import Flask
from flask_restful import Api
from resources.area import Area
from resources.report import Report
from resources.user import User
from resources.venue import Venue

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = 'testing' #wont be production key :)

#create db using sql-alchemy
@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Area, '/area/<string:name>')
#FIXME: these endpoints will not work yet
api.add_resource(Report, '/report/<string:name>')
api.add_resource(User, '/user/<string:name>')
api.add_resource(Venue, '/venue/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)


#TODO:
#Add post endpoints
#Add data and test get endpoints


