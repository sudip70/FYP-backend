from flask import Blueprint, request
from src.medicsdb import Users, db
from src.Methods.form_validation import validate_email, success_false
from flask_jwt_extended import create_access_token

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route('/signup/',methods=['POST'])
def signup():
    request_data = request.get_json()
    try:
        name = request_data['name']
        email = request_data['email']
        password = request_data['password']

        #to carry furthure process if request is valid
        if len(name) > 100:
            return success_false(msg="Name should be less than 100 characters.")
        if len(email) > 100:
            return success_false(msg="Email shouldnt be longer that 100 characters.")
        if len(password) > 20:
            return success_false(msg="Password shouldnt be longer than 20 characters.")
        if not validate_email(email):
            return success_false(msg="Please enter valid email address.")

        #checking if the email aready registered in database.
        if Users.query.filter_by(email=email).first() is not None:
            #if email already exists.
            return success_false(msg="A user with this email adress already exists in our system. \nPlease check the email..")

        users_to_register = Users(name=name, email=email, password=password)
        
        #inserting users in database.
        db.session.add(users_to_register)
        db.session.commit()


        #print(access_token)
        access_token = create_access_token(
            identity=email, expires_delta=False)
        
        
        return {"success": "true", "msg": "Congratulations! \nUser have been registered successfully.", "email": email, "name": name, "access_token": access_token}

    except:
        return success_false()


