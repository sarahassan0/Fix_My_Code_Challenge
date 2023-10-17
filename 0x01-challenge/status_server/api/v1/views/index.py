#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views

# end point ws /api/vi/status wich gives err not found when user request http://0.0.0.0:5000/api/v1/status/
# so the user shoud request  http://0.0.0.0:5000/api/v1/api/v1/status/ to get a suuccessful response
# fix it to /status/


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
