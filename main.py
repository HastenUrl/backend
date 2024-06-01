from dotenv import load_dotenv
from flask import Flask

from lib.kafka import get_kafka

from routes.url import url_route

app = Flask(__name__)

load_dotenv()

app.register_blueprint(url_route)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/kafka-test")
def kafka_connection_test():
    try:
        kfc = get_kafka()
        kfc.produce('test', "This is a sample message")
        if kfc.consume('123', 'test') == "This is a sample message":
            return {"message": "Success"}
    except Exception as e:
        return {"message": str(e)}
    return {"message": "Some error occured"}