import email
from flask import Blueprint, request
from src.medicsdb import Hospitals

hospitals_blueprint = Blueprint('hospitals', __name__)


@hospitals_blueprint.route('/hospitals/', methods=['GET'])
def hospitals():
    if request.method == "GET":
        selected_hospitals = Hospitals.query.all()
        collected_data = hospitals_data(selected_hospitals)
        return {
            "hospitals": collected_data
        }

def hospitals_data(data):
    hospitals = []
    for each in data:
        hospitals.append({
            "hosp_id":each.hosp_id,
            "Name":each.name,
            "Phone":each.phone,
            "Address":each.address,
            "Email":each.email,
            "Website":each.website
        })
    return {"succes":"true", "hospitals": hospitals, "msg": "hospital details loaded successfully"}

