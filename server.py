from flask import Flask, request
from flask_restx import Api, Resource
from scrap import Scrap

app = Flask(__name__)
api = Api(app)

api.add_namespace(Scrap, '/scraps')

if __name__ == "__main__":
    app.run()