from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello World!!!"

@app.route("/create/database/<database_name>", methods=['put'])
def create_database(database_name):
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    #database_name = 'testdb'
    url = 'http://admin:admin@192.168.100.19:5984/' + database_name
    headers = {"Content-Type" : "application/json"}
    r = requests.put(url, headers=headers)
    json_data =   r.json()
    return "good"

@app.route("/delete/database/<database_name>", methods=['DELETE'])
def delete_database(database_name):
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    #database_name = 'testdb'
    url = 'http://admin:admin@192.168.100.19:5984/' + database_name
    headers = {"Content-Type" : "application/json"}
    r = requests.delete(url, headers=headers)
    json_data =   r.json()
    return "good"

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port = 5000)

