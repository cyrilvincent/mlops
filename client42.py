import http.client
import json
import flask
import client42thread

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
port = sock.getsockname()[1]
sock.close()
app: flask.Flask = flask.Flask(__name__)

thread = client42thread.Client42Thread(app, port)
thread.start()

@app.route("/ping")
def ping():
    return "ping"


conn = http.client.HTTPConnection("localhost:5000") # HTTPSConnection
header = {'Content-type':'application/json'}
data = {'host':f'localhost:{port}','route':'/ping', 'isSSL':False}
jsonData = json.dumps(data)
conn.request("POST", "/service42",body=jsonData,headers=header)
with conn.getresponse() as res:
    print(res.status) #200 < 400
    if res.status < 400:
        try:
            jsonString = res.read()
            res = json.loads(jsonString)
            print(res)
        except BaseException as ex:
            print(ex)
conn.close()



