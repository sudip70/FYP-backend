from flask import Flask
from flask import Blueprint, request
from src.medicsdb import Medical_cond

std_blueprint = Blueprint('std', __name__)


@std_blueprint.route('/std/', methods=['GET'])
def std():
    if request.method == "GET":
        selected_std = Medical_cond.query.filter_by(med_id='med14').all()
        collected_data = std_data(selected_std)
        return {
            "std": collected_data
        }

def std_data(data):
    std = []
    for each in data:
        std.append({
            "med_id":each.med_id,
            "Name":each.name,
            "Description":each.description,
            "Symptoms":each.symptoms,
            "Cure":each.cure
        })
    return {"succes":"true", "std": std, "msg": "std details loaded successfully"}