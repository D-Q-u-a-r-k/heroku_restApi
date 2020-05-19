from flask_restful import Resource
from resources.json_rw import read

class DevsListAll(Resource):
    def get(self):
        return read()

    def post(self):
        pass