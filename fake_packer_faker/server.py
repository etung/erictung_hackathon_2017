#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
from flask import make_response
import false_packer
import json

app = Flask(__name__)

@app.route('/packer_faker/api/v1.0/pack_asin', methods=['OPTIONS'])
def option_interceptor():
    response = make_response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'

    return response, 201

@app.route('/packer_faker/api/v1.0/pack_asin', methods=['POST'])
def pack_asin():
    if not request.json:
        abort(400)
    result = false_packer.pack_fake(json.dumps(request.json))

    response = make_response(jsonify(result))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'

    return response, 201

if __name__ == '__main__':
    app.run(debug=True, host="10.48.129.192", port = 5001)
