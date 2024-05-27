from flask import Flask

from routes.url import url_route

app = Flask(__name__)

app.register_blueprint(url_route)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"