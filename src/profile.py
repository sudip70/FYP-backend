from flask import Blueprint, Flask, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.medicsdb import Users


profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/profile/', methods=['GET'])
@jwt_required()
def profile_view():
    if request.method == "GET":
        unique_email = get_jwt_identity()
        user_now = Users.query.filter_by(email=unique_email).first()
        return {
            "success": "true",
            "name": user_now.name,
            "email": user_now.email
        }