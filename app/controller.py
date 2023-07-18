from flask import jsonify
from flask_restful import Resource

from .model import User


class Hello(Resource):
  def get(self):
    return jsonify({ 'message': 'Hello, World!' })

class Users(Resource):
  def get(self):
    users = User.query.all()
    user_list = [{ 'id': user.id, 'name': user.name, 'email': user.email } for user in users]
    return jsonify(user_list)