from flask import Flask
from flask import jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello World!!!"

@app.route("/create/design/<database_name>", methods=['POST'])
def create_design(database_name):
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    url = 'http://admin:admin@192.168.0.125:5984/' + database_name
    headers = {"Content-Type" : "application/json"}
    
    design = {
        "_id": "_design/name",
        "views": { 
            "get_name": 
                {"map": 
                    "function (doc) {\n  if (doc.type=='admin') {\n    emit(doc.firstname, doc.lastname);\n  }\n}"
                }
        }
    }

    r = requests.post(url, data=json.dumps(design),headers=headers)

    json_data =   r.json()

    return "good"

@app.route("/get/design/<database_name>", methods=['GET'])
def get_all_design(database_name):
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    url = 'http://admin:admin@192.168.0.125:5984/' + database_name
    url += '/_all_docs?startkey="_design/"'
    url += '&endkey="_design0"'
    #url += '&include_docs=true'
    headers = {"Content-Type" : "application/json"}
    response = requests.get(url, headers=headers)
    response = response.json()
    return jsonify(response)

@app.route("/delete/design/<database_name>/<doc_id>/<rev_id>", methods=['DELETE'])
def delete_design(database_name, doc_id, rev_id):
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    url = 'http://admin:admin@192.168.0.125:5984/' + database_name + '/' + doc_id + '?rev='
    url += rev_id
    print url
    headers = {"Content-Type" : "application/json"}
    response = requests.delete(url, headers=headers)
    response = response.json()
    return jsonify(response)

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port = 5000)

