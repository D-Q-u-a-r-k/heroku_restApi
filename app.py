from flask import Flask, render_template
from flask_restful import Api
from resources.clients import Clients
from resources.devs import Devs

app = Flask(__name__)
api = Api(app)

@app.route("/")
def landingPage():
    return render_template("index.html", stringPrint = "Hello World!!")

api.add_resource(Clients, "/clients", "/clients/<client_id>")
api.add_resource(Devs, "/devs")

if __name__ == "__main__":
    app.run(debug=True)