from flask import Blueprint, request
from src.medicsdb import Ambulance

ambulance_blueprint = Blueprint('ambulance', __name__)


@ambulance_blueprint.route('/ambulance/', methods=['GET'])
def ambulance():
    if request.method == "GET":
        selected_ambulance = Ambulance.query.all()
        collected_data = ambulance_data(selected_ambulance)
        return {
            "success": "true",
            "msg": "ambulance details loaded successfully",
            "ambulance": collected_data
        }

def ambulance_data(data):
    ambulance = []
    for each in data:
        ambulance.append({
            "amb_id":each.amb_id,
            "organizaion_name":each.org_name,
            "address":each.address,
            "phone":each.phone
        })
    return ambulance

