from flask import Blueprint, request
from src.medicsdb import Medical_cond

medconlist_blueprint = Blueprint('medconlist', __name__)


@medconlist_blueprint.route('/medconlist/', methods=['GET'])

def medconlist():
    if request.method == "GET":
        selected_medconlist = Medical_cond.query.all()
        collected_data = medconlist_data(selected_medconlist)
        return {
            "succes":"true",
            "msg": " medical condition list loaded successfully",
            "medconlist": collected_data
        }

def medconlist_data(data):
    medconlist = []
    for each in data:
        medconlist.append({
            "med_id":each.med_id,
            "Name":each.name,
            "Description":each.description,
            "Symptoms":each.symptoms,
            "Cure":each.cure
        })
    return medconlist

