import random
from flask import Flask, Response, send_from_directory
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

# Инициализируем сервер, решаем траблы с CORS-политикой
app = Flask(__name__, static_folder='./index/build')
CORS(app)
number = ""

# Раздача реакт-статики
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# SSE EventSource, по одному на процесс (пока соединение не закончено, забивается)
@app.route("/stream")
def stream():
    def respond_to_client():
        while True:
            f = open("file.txt", "r")
            number = f.read()
            data = json.dumps({"number": number})
            yield f"data: {data} \n\n"
            time.sleep(0.5)

    return Response(respond_to_client(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run("localhost", 3000)
    # http_server = WSGIServer(("127.0.0.1", 3000), app)
    # http_server.serve_forever()
