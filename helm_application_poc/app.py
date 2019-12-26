import helm_application_poc

from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, session, Blueprint
from prometheus_flask_exporter import PrometheusMetrics
import os


app = app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.3')

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

@app.route('/', methods=['GET'])
def index():
    dict_resturn = {"message" : "hello"}
    return jsonify(dict_resturn)

@app.route('/envVars', methods=['GET'])
def envVars():
    env_vars = os.popen("env").read()
    env_vars_list = env_vars.split("\n")

    env_dict = { "environment" : [] }

    for env in env_vars_list:
        try:
            temp_dict = {}
            env_key_value = env.split("=")
            temp_dict["Key"] = env_key_value[0]
            temp_dict["Value"] = env_key_value[1]
            env_dict["environment"].append(temp_dict)
        except:
            continue

    return jsonify(env_dict)

@app.route('/health', methods=['GET'])
def health():
    result = os.popen("hostname").read()
    ips = (os.popen("hostname -I").read().strip()).split(" ")
    
    dict_resturn = {"hostname" : result, "Ips" : ips}
    return jsonify(dict_resturn)

app.run(host='0.0.0.0')