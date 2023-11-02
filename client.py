import http.client
import json

conn = http.client.HTTPConnection("localhost:5000") # HTTPSConnection
conn.request("GET", "/")
with conn.getresponse() as res:
    print(res.status) #200 < 400
    if res.status < 400:
        try:
            html = res.read()
            print(html)
        except BaseException as ex:
            print(ex)
conn.close()
conn.request("GET", "/api/designs")
with conn.getresponse() as res:
    print(res.status) #200 < 400
    if res.status < 400:
        try:
            jsonRes = res.read()
            print(jsonRes)
        except BaseException as ex:
            print(ex)
conn.close()

#POST
header = {'Content-type':'application/json'}
data = {'precision':1000,'name':'fromclient'}
jsonData = json.dumps(data)
conn.request("POST","/api/design",body=jsonData,headers=header)
with conn.getresponse() as res:
    print(res.status) #200 < 400
    print(res.reason)

# Multipart
import requests
import requests_toolbelt.multipart.encoder as me # pip install requests_toolbelt

data = me.MultipartEncoder(
    fields={
        "prenom" : "Cyril",
        "nom" : "Vincent",
        "file" : ("stlogo.png", open("stlogo.png","rb"), "text/plain"),
    }
)
res = requests.post("http://localhost:5000/form", data = data, headers={'Content-Type': data.content_type})
print(res.status_code)

