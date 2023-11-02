import flask
from restservice import app

@app.route("/other", methods=["GET"])
def other():
    return "Other"

class FlaskOO:

    app: flask.Flask

    @app.route("/oo", methods=["GET"])
    def oo():
        return "OO"

