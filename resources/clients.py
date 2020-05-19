from flask_restful import reqparse, abort, Api, Resource
from resources.json_rw import read, write

# Sample Data for Testing Only
CLIENTS = read()

# Check client_id is present
def abort_if_client_doesnt_exist(client_id):
    if client_id not in CLIENTS:
        abort(404, message="{} doesn't exist".format(client_id))

parser = reqparse.RequestParser()
parser.add_argument('full_name')
parser.add_argument('email')
parser.add_argument('phone')
parser.add_argument('deadline')
parser.add_argument('services')
parser.add_argument('description')

class ClientsQuery(Resource):
    def get(self, client_id):
        abort_if_client_doesnt_exist(client_id)
        return CLIENTS[client_id]

class ClientsSubmit(Resource):
    def post(self):
        args = parser.parse_args()
        client_id = int(max(CLIENTS.keys()).lstrip('client')) + 1
        client_id = 'client%i' % client_id
        CLIENTS[client_id] = {'Full Name': args['full_name'],
                                'Email': args['email'],
                                'Phone': args['phone'],
                                'Deadline': args['deadline'],
                                'Services': args['services'],
                                'Description': args['description']
                                }
        write(CLIENTS) #update json
        return CLIENTS[client_id], 201