from os import name
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "Hello we're here MOTHERFUCKERSSSS!!!"


if __name__ == "__main__":
    app.run(debug=True)
