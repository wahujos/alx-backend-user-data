#!/usr/bin/env python3
"""
includes endpoints for login and logout.
"""

import os
from api.v1.views import app_views
from models.user import User
from flask import jsonify, request, abort


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    """
    responsible for the user login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user or user == []:
        return jsonify({"error": "no user found for this email"}), 404

    for each_user in user:
        if each_user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(each_user.id)
            response = jsonify(each_user.to_json())
            session_name = os.getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)
            return response
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    Handles the user logging out
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
