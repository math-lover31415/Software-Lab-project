"""
POST /api/v1/auth/login
"""

from flask import Blueprint, jsonify, request

from app.services import auth_services

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    result = auth_services.login(payload)

    if isinstance(result, tuple):
        body, status = result
        return jsonify(body), status

    return jsonify(result), 201