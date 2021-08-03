from flask import Flask, request
from flask_restx import Api, Resource
from flask_cors import CORS
from scrap import Scrap

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_namespace(Scrap, '/scraps')

if __name__ == "__main__":
    app.run(host="0.0.0.0")