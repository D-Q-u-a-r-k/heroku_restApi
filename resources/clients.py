from flask_restful import reqparse, abort, Api, Resource
from resources.json_rw import read, write
from db_helper.insert_values import insert

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

class Clients(Resource):
    def get(self, client_id):
        abort_if_client_doesnt_exist(client_id)
        return CLIENTS[client_id]

    def post(self):
            args = parser.parse_args()
            insert(name = args['full_name'],
                    email = args['email'],
                    phone = args['phone'],
                    deadline = args['deadline'],
                    services = args['services'],
                    description = args['description'])
            return 201