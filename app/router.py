import json
from flask import jsonify

from . import app


@app.route('/swagger.json')
def swagger():
  with open('swagger.json', 'r') as f:
    return jsonify(json.load(f))

@app.route('/swagger1.json')
def swagger1():
  with open('swagger1.json', 'r') as f:
    return jsonify(json.load(f))
