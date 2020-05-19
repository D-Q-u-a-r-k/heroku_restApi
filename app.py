from flask import Flask, render_template
from flask_restful import Api
from resources.clients import ClientsQuery, ClientsSubmit
from resources.devs import DevsListAll

app = Flask(__name__)
api = Api(app)

@app.route("/")
def webPage():
    return render_template("index.html", stringPrint = "Hello World!!")

api.add_resource(ClientsQuery, "/clients/<client_id>")
api.add_resource(ClientsSubmit, "/clients")
api.add_resource(DevsListAll, "/devs")

if __name__ == "__main__":
    app.run(debug=True)

