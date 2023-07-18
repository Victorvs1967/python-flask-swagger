from flask import Flask
from flask_restful import Api

from .controller import Hello, Users
from .swagger import SWAGGER_URL, swaggerui_blueprint
from .model import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)
api.add_resource(Hello, '/hello')
api.add_resource(Users, '/users')

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


from .router import *