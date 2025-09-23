from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello World"

@app.route("/alive")
def alive():
    return "Alive"

@app.route("/echo/<message>")
def echo(message):
    return f"Echo: {message}"

@app.route("/bidon")
def bidon():
    values = [1,2,3]
    return jsonify(values)

# House passer une surface dans l'url et retourner le loyer
# Cancer

if __name__ == '__main__':
    app.run()
