from flask_restful import reqparse, abort, Api, Resource

CLIENTS = {
    'client1': {'task': 'build an API'},
    'client2': {'task': '?????'},
    'client3': {'task': 'profit!'},
}

def abort_if_client_doesnt_exist(todo_id):
    if client_id not in CLIENTS:
        abort(404, message="Todo {} doesn't exist".format(client_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


class Clients(Resource):
    def get(self):
        return {"clients": "working"}

    def post(self):
        pass