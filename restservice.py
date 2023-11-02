import flask
import jsonpickle
import mockrepository
import entities

app: flask.Flask = flask.Flask(__name__)

menusdb = [
    {'entree':"Salade", 'plat':"Pâtes carbonara", "dessert":"Fondant au chocolat"},
    {'entree':"Bruschetta", 'plat':"Pizza Marguerite", "dessert":"Pannacotta"},
    {'entree':"Bruschetta", 'plat':"Pizza Marguerite", "dessert":None},
]

class Menu:

    def __init__(self, entree, plat, dessert):
        self.entree = entree
        self.plat = plat
        self.dessert = dessert

@app.route("/")
def hello():
    return "Hello World 2!!"

@app.route("/html")
def html():
    return """
    <html>
        <body>
            <h1>Formation REST</h1>
            <p>Welcome !!!</p>
            <p><font color='red'>Hello <i>World</i></font></p>
        </body>
    </html>
    """

@app.route("/plain")
def plain():
    s = "Texte brut"
    return flask.Response(s,mimetype="text/plain")

@app.route("/firstjson")
def firstJson():
    json = '{"name":"cyril"}'
    return flask.Response(json, mimetype="application/json")

@app.route("/logost")
def logost():
    with open("stlogo.png","rb") as f:
        logo = f.read()
        return flask.Response(logo, mimetype="image/png", status=201)

@app.route("/menus")
def menus():
    return flask.jsonify(menusdb)

@app.route("/mockmenu")
def mockmenu():
    menu = Menu(None, "Gnocchis", "Pannacotta")
    return flask.jsonify(menu.__dict__)

@app.route("/mockmenupickle")
def mockmenupickle():
    menu = Menu(None, "Gnocchis", "Pannacotta")
    json = jsonpickle.encode(menu, unpicklable=False)
    return flask.Response(json, mimetype="application/json")

@app.route("/doc")
def doc():
    s = """
GET /api/designs/all
GET /api/designs/precision/1000
GET /api/designs/layer/114
    """
    return flask.Response(s, mimetype="text/plain")

@app.route("/autodoc")
def autodoc():
    s="<html><body>"
    for rule in app.url_map.iter_rules():
        s += f"{rule.methods} <a href='http://localhost:5000{rule}'>{rule}</a> {rule.arguments}<br/>"
    s+="</body></html>"
    return s


def jsonify(obj):
    json = jsonpickle.encode(obj, unpicklable=False)
    return flask.Response(json, mimetype="application/json")

@app.route("/api/designs/all")
@app.route("/api/designs")
def getAll():
    return jsonify(mockrepository.getAll())

@app.route("/api/designs/precision/<int:precision>")
@app.route("/api/designs/precision/<float:precision>")
def getByPrecision(precision):
    return jsonify(mockrepository.getDesignByPrecision(precision))

@app.route("/api/designs/layer/<int:number>")
def getByLayerNumber(number):
    return jsonify(mockrepository.getDesignByLayerNumber(number))

@app.route("/api/design/<name>")
def getByName(name):
    try:
        design = mockrepository.getDesignByName(name)
        return jsonify(design)
    except IndexError:
        return flask.abort(404)

@app.route("/api/design", methods=["POST"])
def createDesign():
    # data = flask.Request.data RAW data
    json = flask.request.json
    design = entities.Design()
    design.__dict__ = json
    mockrepository.insert(design)
    return flask.jsonify(success=True)

@app.route("/api/design", methods=["PUT"])
def updateDesign():
    json = flask.request.json
    try:
        mockrepository.updateByJSON(json)
    except IndexError:
        return flask.abort(404)
    return flask.jsonify(success=True)

@app.route("/api/design/<name>", methods=["PUT"])
def updateDesign2(name):
    pass

@app.route("/api/design/<name>", methods=["DELETE"])
def deleteDesign(name):
    try:
        mockrepository.delete(name)
    except IndexError:
        return flask.abort(404)
    return flask.jsonify(success=True)

@app.route("/api/designs", methods=["PATCH"])
def getNames():
    return flask.jsonify(mockrepository.getNames())

# http://localhost:5000/api/designs/get?name=Toto&key=value limitée à 1024 caracteres
@app.route("/api/designs/get/<param>", methods=["GET", "POST", "PUT", "DELETE"])
def getByUrlParameter(param):
    s = param
    s += flask.request.args.get("name")
    return s

@app.route("/api/designs/post", methods=["POST"])
def getByJSON():
    json = flask.request.json
    return json

@app.route("/form", methods=["POST"])
def form():
    prenom = flask.request.form["prenom"]
    nom = flask.request.form["nom"]
    file = flask.request.files["file"]
    if file != None:
        print("Found file")
        file.save("static/upload.png")
    return f"{prenom} {nom}"

@app.before_request
def beforeRequest():
    language = flask.request.cookies.get('user_lang')
    if language is None:
        language = "Fr-fr"

        # @flask.after_this_request
        # def remember_language(response):
        #     response.set_cookie('user_lang', language)

@app.route("/shutdown", methods=["GET"])
def shutdown():
    func = flask.request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

import http.client
@app.route("/service42", methods=["POST"])
def service42():
    json = flask.request.json
    host = json["host"]
    route = json["route"]
    isSSL = json["isSSL"]
    conn = http.client.HTTPConnection(host)
    try:
        conn.request("GET", route)
        with conn.getresponse() as res:
            if res.status == 200:
                return flask.jsonify({"status":True})
            else:
                return flask.jsonify({"status": False, "polling": 10})
    except:
        return flask.jsonify({"status": False, "polling": 10})
    finally:
        conn.close()

if __name__ == '__main__':
    app.debug = True
    #app.run() # http://locahost:5000
    import othermodule
    othermodule.FlaskOO.app = app
    from othermodule import *
    app.run(host='0.0.0.0', port=5000, threaded=True)
    #app.run(host='0.0.0.0', port=0, threaded=True)



