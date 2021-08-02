from flask import Flask, request
from flask_restx import Resource, Api, Namespace
import crawler

Scrap = Namespace('Scrap')
@Scrap.route('/')
class ScrapWelcome(Resource):
    def get(self):
        scrap = ""
        
        scrap = request.args.get('NL','knu')
        
        if crawler.scripts(scrap) != None:
            print('OK')

        return crawler.scripts(scrap)