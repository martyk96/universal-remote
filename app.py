#!/usr/bin/python

import RPi.GPIO as GPIO
import logging
import subprocess
from flask import Flask, render_template, request, jsonify,make_response

log_file = 'remote.log'
logging.basicConfig(filename=log_file,level=logging.DEBUG)

app = Flask(__name__)

@app.route("/<device>/<action>",methods=['POST'])
def action(device,action):
    call_resp = subprocess.call(["irsend","SEND_ONCE",device,action])
    if call_resp:
        response = {
                "call":"success",
                "device":device,
                "action":action
        }            
        return jsonify({'response':response}),200
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
