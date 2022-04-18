from flask import Blueprint, request
from src.medicsdb import Medical_cond

medconlist_blueprint = Blueprint('medconlist', __name__)


@medconlist_blueprint.route('/medconlist/', methods=['GET'])
def medconlist():
    if request.method == "GET":
        selected_medconlist = Medical_cond.query.all()
        collected_data = medconlist_data(selected_medconlist)
        return {
            "medconlist": collected_data
        }

def medconlist_data(data):
    medconlist = []
    for each in data:
        medconlist.append({
            "med_id":each.med_id,
            "Name":each.name,
        })
    return {"succes":"true", "medconlis": medconlist, "msg": " medical condition list loaded successfully"}

