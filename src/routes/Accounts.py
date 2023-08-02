from flask import Blueprint, jsonify, request, redirect, url_for
from werkzeug.security import generate_password_hash
#entties
from models.entities.Accounts import Accounts
from models.entities.Turns import Turns
# Models
from models.AccountsModel import AccountsModel
from models.TurnsModel import TurnsModel
from models.CatTurnsModel import CatTurnsModel
#blueprint
account = Blueprint('account', __name__,)

@account.route('/')
def index():
    return redirect(url_for('login'))

@account.route('/registry', methods=['POST'])
def registryAccount():
    try:
        name = request.json['nombre']
        email = request.json['correo']
        password = request.json['contrasena']
        idCatAccountType = request.json['id_cat_tipo_cuenta']      
        hash=generate_password_hash(str(password))
        account = Accounts(name,email, hash, idCatAccountType)
        _account=AccountsModel.registry(account)
        classification_turns = CatTurnsModel.classification_turns(idCatAccountType)
        turns= Turns(_account.id_cuenta, classification_turns)
        _turn= TurnsModel.registry(turns)
        return {"status":"account registered successfully"}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 
    
    
@account.route('/login', methods=['GET', 'POST'])
def login():
    try:
       if request.method=='POST':
           email = request.json['correo']
           password = request.json['contrasena']
           data_account = Accounts("", email, password, 0)
           logged_account= AccountsModel.login(data_account)
           if logged_account != None:
               if logged_account.contrasena:
                  return {"Account logged":200} 
               else:
                   return {"Invalid password":500}
           else:    
            return {"Account not found":404}
       else:        
            return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 