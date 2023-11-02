import threading
import flask

class Client42Thread(threading.Thread):

    def __init__(self, app, port):
        super().__init__()
        self.app = app
        self.port = port

    def run(self):
        self.app.run(port=self.port)

    #Voir si on peut faire un cb quand werkzeurg s'est lancé

