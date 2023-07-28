from database.db import db
from werkzeug.security import check_password_hash


class Accounts(db.Model):
    __tablename__ = 'cuentas'

    id_cuenta = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(102), nullable=False)
    id_cat_tipo_cuenta = db.Column(db.SmallInteger, db.ForeignKey('cat_tipo_cuenta.id_cat_tipo_cuenta'))
    
    

    def __init__(self, nombre=None, correo=None, contrasena=None, id_cat_tipo_cuenta=None):
        self.nombre=nombre
        self.correo=correo
        self.contrasena=contrasena
        self.id_cat_tipo_cuenta=id_cat_tipo_cuenta

        
    def to_json(self):
        return {
        'id_cuenta': self.id_cuenta,   
        'nombre': self.nombre,
        'correo': self.correo,
        'contrasena': self.contrasena,
        'id_cat_tipo_cuenta': self.id_cat_tipo_cuenta,
        }
    @classmethod    
    def check_password(self, hashed_password, password):
        
        return check_password_hash(hashed_password, password)   