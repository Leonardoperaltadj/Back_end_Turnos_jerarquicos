from flask import Blueprint, jsonify, request
#entities
from models.entities.catAccountTypes import CatAccountTypes
# Models
from models.catAccountTypesModel import CatAccountTypesModel
#blueprint
CatAccountType = Blueprint('accountType', __name__,)

@CatAccountType.route('/registry', methods=['POST'])
def registryTypeAccount():
    try:
        idCatAccountType = request.json['id_cat_tipo_cuenta']
        account = request.json['cuenta']     

        accountType = CatAccountTypes(idCatAccountType, account)
        CatAccountTypesModel.registry(accountType)
       
        return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 