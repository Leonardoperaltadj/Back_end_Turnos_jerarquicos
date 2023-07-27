from database.db import db

class Accounts(db.Model):
    __tablename__ = 'cuentas'

    id_cuenta = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    id_cat_tipo_cuenta = db.Column(db.SmallInteger, db.ForeignKey('cat_tipo_cuenta.id_cat_tipo_cuenta'))
    
    

    def __init__(self, nombre, correo, contrasena, id_cat_tipo_cuenta):
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