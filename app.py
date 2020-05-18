from flask import Flask, render_template, request
from flask_restful import Api
from resources.clients import Clients
from resources.devs import Devs

app = Flask(__name__)
api = Api(app)

@app.route("/")
def webPage():
    return render_template("index.html", stringPrint = "Hello World!!")

api.add_resource(Clients, "/clients")
api.add_resource(Devs, "/devs")

if __name__ == "__main__":
    app.run(debug=True)