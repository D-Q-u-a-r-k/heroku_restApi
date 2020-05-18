from flask_restful import Resource

class Devs(Resource):
    def get(self):
        return {"devs": "working"}

    def post(self):
        pass