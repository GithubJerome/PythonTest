from flask import Flask
from flask import jsonify
import requests
import json
# ------------ swagger ------------ #
from flasgger import Swagger
from flask import request
# ------------ swagger ------------ #

app = Flask(__name__)
# ------------ swagger ------------ #
Swagger(app)
# ------------ swagger ------------ #
ip = '192.168.22.9'
database_name = 'test'

@app.route("/")
def test():
    return "Hello World!!!"

@app.route("/create/document", methods=['post'])
def create_document():
    # ------------ swagger ------------ #
    """
    This API is for Creating Documents
    ---
    tags:
      - Create
    produces:
      - application/json
    parameters:
      - name: firstname
        in: query
        description: Firstname
        required: true
        type: string
      - name: lastname
        in: query
        description: Lastname
        required: true
        type: string
      - name: address
        in: query
        description: Address
        required: true
        type: string
      - name: type
        in: query
        description: Type
        required: true
        type: string
    responses:
      500:
        description: Error
      200:
        description: Creating documents
    """
    data = {}
    data['firstname'] = request.args.get('firstname')
    data['lastname'] = request.args.get('lastname')
    data['address'] = request.args.get('address')
    data['type'] = request.args.get('type')
    # ------------ swagger ------------ #
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    url = 'http://admin:admin@' + ip + ':5984/' + database_name

    headers = {"Content-Type" : "application/json"}

    r = requests.post(url, data=json.dumps(data),headers=headers)

    json_data =   r.json()

    return "Good!"


@app.route("/read/document", methods=['get'])
def read_document():
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    
    url = 'http://admin:admin@' + ip + ':5984/' + database_name
    
    headers = {"Content-Type" : "application/json"}

    # GET MODULE
    firstname = 'Mark'
    lastname = 'Rizal'
    url += '/_design/employee/_view/admin'
    url += '?key="' + lastname + '"'
    print url
    # EXECUTE COUCH QUERY
    res = requests.get(url)

    json_data = res.json()
    print json_data 
    if json_data['rows']:
        return jsonify(json_data['rows'])
    return 'Bad!'



@app.route("/update/document", methods=['put'])
def update_document():
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    data = {}
    data['firstname'] = 'Roel'
    data['lastname'] = 'San Jose'
    data['address'] = 'Palawan'
    data['type'] = 'admin'
    data['_rev'] = '1-175ad67e5ec8560211bbe7bc16ceebb0'

    url = 'http://admin:admin@' + ip + ':5984/' + database_name
    url += '/d3ea3c5f94f38cafb1b0bdea15001337'

    headers = {"Content-Type" : "application/json"}

    r = requests.put(url, data=json.dumps(data),headers=headers)

    json_data =   r.json()
    return "Good!"



@app.route("/delete/document", methods=['delete'])
def delete_document():
    doc_id = 'd3ea3c5f94f38cafb1b0bdea15001337'
    doc_rev = '2-cf8ddb7467d066644e0792e1dfc0ab50' # GET NEW REV NUMBER
    # PROTOCOL://USER:PASSWORD@HOST:PORT/
    url = 'http://admin:admin@' + ip + ':5984/' + database_name
    url += '/' + doc_id + '?' + 'rev=' + doc_rev 
    headers = {"Content-Type" : "application/json"}
    response = requests.delete(url, headers=headers)
    response = response.json()
    return "Delete!"

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port = 5000)

