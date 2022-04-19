from flask import Blueprint, request
from src.medicsdb import blood_req

bloodreq_blueprint = Blueprint('bloodreq', __name__)


@bloodreq_blueprint.route('/bloodreq/', methods=['GET'])
def bloodreq():
    if request.method == "GET":
        selected_bloodreq = blood_req.query.all()
        collected_data = bloodreq_data(selected_bloodreq)
        return {
            "succes":"true",
            "msg": "blood request loaded successfully",
            "bloodreq": collected_data
        }

def bloodreq_data(data):
    blood_req = []
    for each in data:
        blood_req.append({
            "blood_id":each.blood_id,
            "Name":each.name,
            "Phone": each.phone,
            "Location":each.location,
            "Blood_Group":each.blood_group
        })
    return blood_req

