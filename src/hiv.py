from flask import Flask
from flask import Blueprint, request
from src.medicsdb import Medical_cond

hiv_blueprint = Blueprint('hiv', __name__)


@hiv_blueprint.route('/hiv/', methods=['GET'])
def hiv():
    if request.method == "GET":
        selected_hiv = Medical_cond.query.filter_by(med_id='med13').all()
        collected_data = hiv_data(selected_hiv)
        return {
            "succes":"true",
            "msg": "hiv details loaded successfully",
            "hiv": collected_data
        }

def hiv_data(data):
    hiv = []
    for each in data:
        hiv.append({
            "med_id":each.med_id,
            "Name":each.name,
            "Description":each.description,
            "Symptoms":each.symptoms,
            "Cure":each.cure
        })
    return hiv