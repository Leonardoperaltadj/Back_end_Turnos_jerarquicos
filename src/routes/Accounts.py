from flask import Blueprint, jsonify, request
#entities
from models.entities.Accounts import Accounts
# Models
from models.AccountsModel import AccountsModel
#blueprint
account = Blueprint('account', __name__,)

@account.route('/registry', methods=['POST'])
def registryAccount():
    try:
        name = request.json['nombre']
        email = request.json['correo']
        password = request.json['contrasena']
        idCatAccountType = request.json['id_cat_tipo_cuenta']      

        account = Accounts(name,email, password, idCatAccountType)
        AccountsModel.registry(account)
       
        return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 