from flask import Blueprint, request
from src.medicsdb import blood_req, db
from src.Methods.form_validation import success_false
from flask_jwt_extended import jwt_required, get_jwt_identity

postreq_blueprint = Blueprint('postreq', __name__)

@postreq_blueprint.route('/postreq/',methods=['POST'])
@jwt_required()
def bloodrequest():
    request_data = request.get_json()
    try:
        name = request_data['name']
        phone = request_data['phone']
        location = request_data['location']
        blood_group = request_data['blood_group']

        #to carry furthure process if request is valid
        if len(name) > 50:
            return success_false(msg="Name should be less than 50 characters.")
        if len(name) < 1:
            return success_false(msg="Name can not be empty.")
        if len(phone) > 15:
            return success_false(msg="Phone shouldnt be longer that 50 characters.")
        if len(phone) < 1:
            return success_false(msg="Phone Number can not be empty.")
        if len(location) > 50:
            return success_false(msg="Location shouldnt be longer than 50 characters.")
        if len(location) < 1:
            return success_false(msg="Location can not be empty.")
        if len(blood_group) > 3:
            return success_false(msg="Blood Group shouldnt be longer than 3 characters.")
        if len(blood_group) < 1:
            return success_false(msg="Blood Group can not be empty.")


        post_req = blood_req(name=name, phone=phone, location=location, blood_group=blood_group)
        
        #inserting users in database.
        db.session.add(post_req)
        db.session.commit()
        
        
        return {"success": "true", "msg": "Your Blood request has been added!!", "Phone": phone, "Name": name, "Location":location, "Blood Group":blood_group}

    except:
        return success_false()