from flask import Blueprint, jsonify, request, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user
from app import login_manager_app
from cryptography.fernet import Fernet
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
key= Fernet.generate_key()
object_encrypt=Fernet(key)

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
        account = Accounts(None,name,email, hash, idCatAccountType)
        _account=AccountsModel.registry(account)
        return {"status":"account registered successfully"}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 
    
    
@account.route('/login', methods=['GET', 'POST'])
def login():
    try:
       if request.method=='POST':
           email = request.json['correo']
           password = request.json['contrasena']
           data_account = Accounts( None,"", email, password, 0)
           logged_account= AccountsModel.login(data_account)
           if logged_account != None:
               if logged_account.contrasena:
                  login_user(logged_account, remember=True)
                  #id= str(logged_account.id_cuenta)
                  #text_encrypt=object_encrypt.encrypt(str.encode(id)) 
                  id=int(logged_account.id_cuenta)
                  return jsonify({"Account logged":200, "id_account":id})#text_encrypt.decode('utf-8')})#, redirect(url_for('account.turn'))
               else:
                   return {"Invalid password":500}
           else:    
            return {"Account not found":404}
       else:        
            return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 
    
@account.route('/turn/<id>', methods=['GET','POST'])
def turn(id):
    try:
        
        #id_convert=str.encode(id)
        #decryption_bytes=object_encrypt.decrypt(id_convert)
        #decryption = decryption_bytes.decode()
        #id=int(decryption)
        
        data_account=AccountsModel.get_account(id)
        classification_turns = CatTurnsModel.classification_turns(data_account.id_cat_tipo_cuenta)
        turns= Turns(data_account.id_cuenta, classification_turns)
        _turn= TurnsModel.registry(turns)
        #data_turn.append(data_account)
        if _turn != None:
            data_turn=TurnsModel.get_account_turn()
            return jsonify(data_turn)
        else:
            data_turn=TurnsModel.get_account_turn()
            return jsonify({"Turnos_duplicado":200},data_turn)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500     