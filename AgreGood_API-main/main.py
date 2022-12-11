from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from decider import Decider

app = Flask(__name__)
api = Api(app)

@app.route('/api/get', methods = ['GET'])
def get():
    args = request.args

    nit = int(args.get("nitrogen"))
    phos = int(args.get("phosphorus"))
    pot = int(args.get("potassium"))
    temp = int(args.get("temperature"))
    hum = int(args.get("humidity"))
    ph = float(args.get("ph"))
    rainfall = int(args.get("rainfall"))

    crop_name = Decider(nit, phos, pot, temp, hum, ph, rainfall)

    return crop_name

if __name__ == '__main__':
    app.run(port = 5003)