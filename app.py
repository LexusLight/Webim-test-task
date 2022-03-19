import json
import time
import os
from flask import Flask, Response, send_from_directory
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

# Инициализируем сервер, решаем траблы с CORS-политикой
app = Flask(__name__, static_folder='./index/build')
CORS(app)


# Раздача статики
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


#
# @app.route("/test")
# def test():
#     f = open('text.txt', 'r')
#     res = f.read()
#     return res

@app.route("/stream")
def stream():
    def respond_to_client():
        while True:
            f = open('text.txt', 'r')
            number = f.read()
            data = json.dumps({"number": number})
            yield f"data: {data} \n\n"
            r = open('text.txt', 'w')
            r.write(1+number)
            time.sleep(1)
    return Response(respond_to_client(), mimetype='text/event-stream')


if __name__ == "__main__":
    #app.run("localhost", 3000)
    http_server = WSGIServer(("", 3000), app)
    http_server.serve_forever()
