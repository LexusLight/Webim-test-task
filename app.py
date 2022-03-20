import json
import time
import os

import psycopg2
from flask import Flask, Response, send_from_directory
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
import worker
monkey.patch_all()

# Инициализируем сервер, решаем траблы с CORS-политикой
app = Flask(__name__, static_folder='./index/build')
CORS(app)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

# Раздача статики
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

def get_number():
    query = "SELECT number FROM numbers WHERE id=1"
    cur.execute(query)
    num = cur.fetchall()
    num = num[0][0]
    return num

@app.route("/stream")
def stream():
    def respond_to_client():
        while True:
            number = get_number()
            data = json.dumps({"number": number})
            yield f"data: {data} \n\n"
            time.sleep(1)
    return Response(respond_to_client(), mimetype='text/event-stream')


if __name__ == "__main__":
    #app.run("localhost", 3000)
    connect()
    http_server = WSGIServer(("", 3000), app)
    http_server.serve_forever()
