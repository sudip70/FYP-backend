from flask import Blueprint, request
from src.medicsdb import Medical_cond

med_condition_blueprint = Blueprint('med_condition', __name__)

@med_condition_blueprint.route('/med_condition/', methods=['GET'])
def med_condition():
    if request.method == "GET":
        search_con = request.args.get('con')
       # request_data = request.get_json()
       # name = request_data['name']
        medical_condition = Medical_cond.query.filter_by(name=search_con).all()
        collected_data = med_data(medical_condition)
        return {
            "succes":"true",
            "msg": "medical condition details loaded successfully",
            "med_condition": collected_data
        }
def med_data(data):
    med_con = []
    for each in data:
        med_con.append({
            "med_id":each.med_id,
            "name":each.name,
            "description":each.description,
            "symptoms":each.symptoms,
            "cure":each.cure
        })
    return med_con

