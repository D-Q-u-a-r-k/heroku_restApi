from flask_restful import reqparse, abort, Api, Resource
from resources.json_rw import read, write

# Sample Data for Testing Only
CLIENTS = read()

# Check client_id is present
def abort_if_client_doesnt_exist(client_id):
    if client_id not in CLIENTS:
        abort(404, message="Todo {} doesn't exist".format(client_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class ClientsQuery(Resource):
    def get(self, client_id):
        abort_if_client_doesnt_exist(client_id)
        return CLIENTS[client_id]

class ClientsSubmit(Resource):
    def post(self):
        args = parser.parse_args()
        client_id = int(max(CLIENTS.keys()).lstrip('client')) + 1
        client_id = 'client%i' % client_id
        CLIENTS[client_id] = {'task': args['task']}
        write(CLIENTS) #update json
        return CLIENTS[client_id], 201