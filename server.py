from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def webPage():
    return render_template("index.html", stringPrint = "Hello World!!")

if __name__ == "__main__":
    app.run(debug=True)