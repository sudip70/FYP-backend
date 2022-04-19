from sre_constants import SUCCESS
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Methods.form_validation import success_false
from src.medicsdb import Users, db

account_del_blueprint = Blueprint('account_del', __name__)


@account_del_blueprint.route('/account_del/', methods=['DELETE'])
@jwt_required()
def accountDel():
    if request.method == "DELETE":
        #try:
        user_email = get_jwt_identity()
        user = Users.query.filter_by(email=user_email).first()
        delete_user = Users.query.get(user.user_id)
        db.session.delete(delete_user)
        db.session.commit()
        return {"success": "true", "msg": "User deleted"}
        #except:
        return success_false()

