from flask import Blueprint, request
from src.medicsdb import Doctors

doctors_blueprint = Blueprint('doctors', __name__)


@doctors_blueprint.route('/doctors/', methods=['GET'])
def doctor():
    if request.method == "GET":
        selected_doctor = Doctors.query.all()
        collected_data = doctor_data(selected_doctor)
        return {
            "succes":"true",
            "msg": "doctors details loaded successfully",
            "doctors": collected_data
        }

def doctor_data(data):
    doctor = []
    for each in data:
        doctor.append({
            "doc_id":each.doc_id,
            "name":each.name,
            "email":each.email,
            "phone":each.phone,
            "hospital":each.Hospital,
            "specialization":each.specialization
        })
    return doctor