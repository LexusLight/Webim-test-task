import json
import time
import os
import random
from threading import *
from flask import Flask, Response, send_from_directory
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

# Инициализируем сервер, решаем траблы с CORS-политикой
app = Flask(__name__, static_folder='./index/build')
CORS(app)
number = "777"


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Поток эвентов для бедных
@app.route("/stream")
def stream():
    def respond_to_client():
        while True:
            data = json.dumps({"number": number})
            yield f"data: {data} \n\n"
            time.sleep(1)

    return Response(respond_to_client(), mimetype='text/event-stream')

@app.route("/test")
def test():
    return number

# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
def random_number():
    while True:
        global number
        time.sleep(5.0)
        number = random.randint(100000, 999999)

thread = Thread(target=random_number)
thread.start()
        
#При запуске скрипта, создаётся поток для выдачи рандом номера, запускается листенер сервера.
if __name__ == "__main__":
    #app.run("localhost", 3000)
    http_server = WSGIServer(("", 3000), app)
    http_server.serve_forever()
