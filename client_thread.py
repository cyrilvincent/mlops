import datetime
import threading
import json
import requests

class ClientThread(threading.Thread):

    def __init__(self, num, url):
        super().__init__()
        self.num = num
        self.url = url

    def run(self):
        with open(f"data/mnist/mnist_{self.num % 10}.json") as f:
            x = json.load(f)
        r = requests.post(self.url, json=x)
        print(f"Thread {self.num} => {r.content}")

if __name__ == '__main__':
    nb_thread = 100
    url = 'http://127.0.0.1:5000/mnist'
    pool = []
    for i in range(nb_thread):
        thread = ClientThread(i, url)
        pool.append(thread)
    time0 = datetime.datetime.now()
    print(f"Start {url} with {nb_thread} threads")
    for thread in pool:
        thread.start()
    for thread in pool:
        thread.join()
    span = datetime.datetime.now() - time0
    print(f"End in {span.total_seconds()}s")

    url = 'http://127.0.0.1:80/mnist'
    pool = []
    for i in range(nb_thread):
        thread = ClientThread(i, url)
        pool.append(thread)
    time0 = datetime.datetime.now()
    print(f"Start {url} with {nb_thread} threads")
    for thread in pool:
        thread.start()
    for thread in pool:
        thread.join()
    span = datetime.datetime.now() - time0
    print(f"End in {span.total_seconds()}s")




