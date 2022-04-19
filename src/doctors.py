from flask import Blueprint, request
from src.medicsdb import Doctors

doctors_blueprint = Blueprint('doctors', __name__)


@doctors_blueprint.route('/doctors/', methods=['GET'])
def doctors():
    if request.method == "GET":
        selected_doctors = Doctors.query.all()
        collected_data = doctors_data(selected_doctors)
        return {
            "succes":"true",
            "msg": "doctors details loaded successfully",
            "doctors": collected_data
        }

def doctors_data(data):
    doctors = []
    for each in data:
        doctors.append({
            "doc_id":each.doc_id,
            "Name":each.name,
            "Email":each.email,
            "Phone":each.phone,
            "Hospital":each.Hospital,
            "Specialization":each.specialization
        })
    return doctors