from flask import Flask, request
from flask_restx import Resource, Api, Namespace
import crawler

Scrap = Namespace('Scrap')
@Scrap.route('/')
class ScrapWelcome(Resource):
    def get(self):
        scrap = ""
        
        scrap = request.args.get('NL','knu')
        data = crawler.scripts(scrap)
        
        if  data != None:
            print('OK')

        return data