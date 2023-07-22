from flask import Blueprint, jsonify, request
#entities
from models.entities.User import User
# Models
from models.UserModel import UserModel
from database.db import db

usuario = Blueprint('usuario', __name__,)

@usuario.route('/',methods=['GET'])
def get_users():
    try:
        users=UserModel.get_users()
       
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@usuario.route('/viewuser',methods=['GET'])
def get_user():
    try:
        id_user = int(request.json['id_usuario'])
        user=UserModel.get_user(id_user)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500    
    
@usuario.route('/registryuser', methods=['POST'])
def registry_users():
    try:
        id_usuario = int(request.json['id_usuario'])
        nombre = request.json['nombre']
        apellido_pa = request.json['apellido_pa']
        apellido_ma = request.json['apellido_ma']
        username = request.json['username']
        telefono = request.json['telefono']
        contrasena = request.json['contrasena']
        id_cat_rol = int(request.json['id_cat_rol'])
        id_cat_estatus = int(request.json['id_cat_estatus'])

        user = User(id_usuario,nombre,apellido_pa, apellido_ma, username, telefono, contrasena, id_cat_rol, id_cat_estatus)
        UserModel.registryUser(user)
       
        return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500    
    
@usuario.route('/deleteuser')
def delete_user():
    try:
        id_user = int(request.json['id_usuario'])
        UserModel.delete_user(id_user)
        return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500      