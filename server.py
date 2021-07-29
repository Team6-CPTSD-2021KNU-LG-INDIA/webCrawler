from flask import Flask, request
from flask_restx import Api, Resource
from scrap import scrap

app = Flask(__name__)
api = Api(app)

api.add_namespace(scrap, '/scrap')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)