import json
import time
import random
from threading import *
from flask import Flask, Response
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
number = ""


@app.route("/")
def render_index():
    return "AAA"


# Шикарная передача эвент сурса. Каждую секунду передаём
@app.route("/stream")
def stream():
    def respond_to_client():
        while True:
            data = json.dumps({"number": number})
            yield f"data: {data} \n\n"
            time.sleep(1)
    return Response(respond_to_client(), mimetype='text/event-stream')


def random_number():
    while True:
        global number
        time.sleep(5.0)
        number = random.randint(100000, 999999)


if __name__ == "__main__":
    thread = Thread(target=random_number)
    thread.start()
    http_server = WSGIServer(("localhost", 1337), app)
    http_server.serve_forever()