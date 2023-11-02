import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello from Cyril : 192.168.25.67"

@app.route("/assembly")
def assembly():
    return flask.Response("Assembly\ntoto",mimetype="text/plain")

@app.route("/xl")
def xl():
    return flask.Response("toto;titi",mimetype="text/csv")

@app.route("/json")
def json():
    json = '{"name":"cyril"}'
    return flask.Response(json, mimetype="application/json")

import math
@app.route("/badhtml")
def badhtml():
    html="""
        <html>
            <title>Hello World!</title>
            <body>
                <H1>Hello World<font color="red">!</font></H1>
                <table border="1">"""
    for i in range(10):
        html += f"<tr><td>{i}</td><td>{math.sin(i / 100)}</td></tr>"

    html+="""   </table>
            </body>
        </html>
    """
    return html

@app.route("/html")
def html():
    user = {"firstName" : "Cyril", "lastName" : "Vincent", "roles" : ["admin", "client"]}
    return flask.render_template("index.html", user=user)

@app.route("/html/<int:param>")
def htmlwithparam(param):
    return flask.render_template("indexwithparam.html", id=param)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)