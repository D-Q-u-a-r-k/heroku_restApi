from flask_restful import Resource

class Clients(Resource):
    def get(self):
        return {"clients": "working"}

    def post(self):
        pass