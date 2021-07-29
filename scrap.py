from flask import request
from flask_restx import Resource, Api, Namespace
import crawler

api = Namespace('scrap')

@api.route('/')
def welcome():
    return "Please input your interest schedule"

@api.route('/scrap')
def post(self):
    scrap = ""
    
    scrap = request.json.get('data')
    
    return crawler.scripts(scrap)


@api.route('/scrap/<str:NL>')
def get(self, id):
    return {
    }