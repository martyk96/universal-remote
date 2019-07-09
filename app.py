#!/usr/bin/python

import RPi.GPIO as GPIO
import logging
from flask import Flask, render_template, request

log_file = 'remote.log'
logging.basicConfig(filename=log_file,level=logging.DEBUG)

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

pins = { 
        23:{'name':'GPIO 23','state':GPIO.LOW},
        24:{'name':'GPIO 24','state':GPIO.LOW}
       }

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)

@app.route("/")
def main():

@app.route("/<device>/<action>")
def action(device,action):

