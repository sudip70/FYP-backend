from flask import Flask
from flask import Blueprint, request
from src.medicsdb import Medical_cond

covid_blueprint = Blueprint('covid', __name__)


@covid_blueprint.route('/covid/', methods=['GET'])
def covid():
    if request.method == "GET":
        selected_covid = Medical_cond.query.filter_by(med_id='med8').all()
        collected_data = covid_data(selected_covid)
        return {
            "covid": collected_data
        }

def covid_data(data):
    covid = []
    for each in data:
        covid.append({
            "med_id":each.med_id,
            "Name":each.name,
            "Description":each.description,
            "Symptoms":each.symptoms,
            "Cure":each.cure
        })
    return {"succes":"true", "covid": covid, "msg": "covid details loaded successfully"}