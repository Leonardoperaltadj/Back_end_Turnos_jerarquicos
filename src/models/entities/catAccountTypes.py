from database.db import db

class catAccountTypes(db.Model):
    __tablename__ = 'cat_tipo_cuenta'

    id_cat_tipo_cuenta = db.Column(db.SmallInteger, primary_key=True)
    cuenta = db.Column(db.String(20), nullable=False)
    #usuarios = db.relationship('User', backref='cat_roles', lazy = True )

    def __init__(self, id_cat_tipo_cuenta, cuenta=None):
        self.id_cat_tipo_cuenta=id_cat_tipo_cuenta
        self.cuenta=cuenta


    def to_json(self):
        return {
        'id_cat_tipo_cuenta': self.id_cat_tipo_cuenta,   
        'cuenta': self.cuenta
        }