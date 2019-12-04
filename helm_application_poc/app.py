import helm_application_poc

from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, session, Blueprint

import os

class App(object):

    def __init__(self):
        self.app = app = Flask(__name__)
        self.flask_init()

    def flask_init(self):    
        self.register_blue_prints()
        self.app.run(host='0.0.0.0')
    
    def register_blue_prints(self):
        self.app.register_blueprint(user_controller)

##Routes

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/', methods=['GET'])
def index():
    dict_resturn = {"message" : "hello"}
    return jsonify(dict_resturn)


@user_controller.route('/health', methods=['GET'])
def health():
    result = os.popen("hostname").read()
    ips = (os.popen("hostname -I").read().strip()).split(" ")
    
    dict_resturn = {"hostname" : result, "Ips" : ips}
    return jsonify(dict_resturn)