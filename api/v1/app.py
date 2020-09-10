#!/usr/bin/python3
""" Status of our API """
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS

"""Host and port env variables"""
host_env = getenv('HBNB_API_HOST') or '0.0.0.0'
port_env = getenv('HBNB_API_PORT') or 5000


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins:": "0.0.0.0"}})
app.register_blueprint(app_views)



@app.teardown_appcontext
def teardown_db(error):
    """ Close db session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ handler error 404 """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(
        host=host_env, port=port_env,
        debug=True, threaded=True,
    )
