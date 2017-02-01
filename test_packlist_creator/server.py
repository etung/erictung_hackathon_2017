#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
from flask import make_response
import json
import pick

app = Flask(__name__)

INVENTORY_FILENAME = "inventory.json"

@app.route('/packlist_creator/api/v1.0/help', methods=['GET'])
def print_help():
    print 

@app.route('/packlist_creator/api/v1.0/get_order', methods=['GET'])
def create_order_no_count():

    with open(INVENTORY_FILENAME, "r" ) as FILE:
        inventory = json.load(FILE)

    packlist = pick.getPacklistFromJson(
        json.dumps(inventory))

    response = make_response(jsonify(packlist))
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response, 201

@app.route('/packlist_creator/api/v1.0/create_order', methods=['POST'])
def create_order():
    if not request.json:
        abort(400)

    with open(INVENTORY_FILENAME, "r" ) as FILE:
        inventory = json.load(FILE)

    if 'count' in request.json :
        orders = []
        for n in xrange(request.json["count"]) :
            packlist = pick.getPacklistFromJson(
                json.dumps(inventory))
            orders.append(packlist)
        return jsonify(orders), 201

    packlist = pick.getPacklistFromJson(
                json.dumps(inventory))

    return jsonify(packlist), 201

@app.route('/packlist_creator/api/v1.0/inventory', methods=['GET'])
def print_inventory():
    with open(INVENTORY_FILENAME, "r" ) as FILE:
        inventory = json.load(FILE)
    return jsonify(inventory), 201

@app.route('/packlist_creator/api/v1.0/update_inventory', methods=['POST'])
def update_inventory():
    if not request.json:
        abort(400)
    with open(INVENTORY_FILENAME, "w" ) as FILE:
        json.dump(request.json, FILE)
    return jsonify(request.json), 201



if __name__ == '__main__':
    app.run(debug=True, host="10.48.129.192")
