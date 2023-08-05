from flask import Blueprint, jsonify, request, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user
from app import login_manager_app
import base64
#entties
from models.entities.Accounts import Accounts
from models.entities.Turns import Turns
# Models
from models.AccountsModel import AccountsModel
from models.TurnsModel import TurnsModel
from models.CatTurnsModel import CatTurnsModel
#blueprint
account = Blueprint('account', __name__,)

@login_manager_app.user_loader
def load_user(id):
    return AccountsModel.get_by_id(id)

@login_manager_app.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = Accounts.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = Accounts.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None

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
                  login_user(logged_account, remember=True)
                  print(current_user.contrasena)
                  return {"Account logged":200}#, redirect(url_for('account.turn'))
               else:
                   return {"Invalid password":500}
           else:    
            return {"Account not found":404}
       else:        
            return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 
    
@account.route('/turn', methods=['GET'])
def turn():
    try:
        data_account=[]
        print(1)
        account= Accounts(current_user.nombre, current_user.correo,current_user.contrasena,current_user.id_cat_tipo_cuenta)
        print(1)
        _account=data_account.append(account.to_json())
        print(1)
            
        return jsonify(_account)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500     