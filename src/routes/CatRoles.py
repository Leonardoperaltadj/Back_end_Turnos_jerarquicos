from flask import Blueprint, jsonify

# Models
from models.CatRolesModel import CatRolesModel

roles = Blueprint('roles', __name__,)

@roles.route('/',)
def get_roles():
    try:
        roles=CatRolesModel.get_roles()
       
        return jsonify(roles)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500