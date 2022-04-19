from flask import Blueprint, request
from src.Methods.form_validation import validate_email, success_false
from src.medicsdb import Users
from flask_jwt_extended import create_access_token

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/login/', methods=['POST'])
def login():
    request_data = request.get_json()
    try:
        email = request_data['email']
        password = request_data['password']

      
        if len(password) > 20:
            return success_false(msg="Password should be less than 20 characters")
        if len(email) > 100:
            return success_false(msg="Email should be less than 100 characters")
        if not validate_email(email):
            print(email)
            return success_false(msg="Please enter a valid email address")

        # now moving to database querying if provided registration data format is correct
        user_login = Users.query.filter_by(email=email).first()

        if user_login:
            # will check password if that user exists
            password_is_correct = Users.query.filter_by(password=password).first()

            if password_is_correct:
                access_token = create_access_token(
                    identity=email, expires_delta=False)
                return {"success": "true", "msg": "Login succesful", "access_token": access_token}
            # if passoword is wrong
            else:
                return success_false(msg="Please provide correct password")
        # if trying user does not exist
        else:
            return success_false(msg="User with this email does not exist in our system")

    except:
        return success_false()
