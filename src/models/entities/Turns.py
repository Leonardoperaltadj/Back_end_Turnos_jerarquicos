from database.db import db

class Turns(db.Model):
    __tablename__ = 'turnos'

    id_turno = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_cuenta = db.Column(db.Integer, db.ForeignKey('cuentas.id_cuenta'))
    id_cat_turno = db.Column(db.SmallInteger, db.ForeignKey('cat_turno.id_cat_turno'))

    def __init__(self, id_cuenta, id_cat_turno):
        self.id_cuenta=id_cuenta
        self.id_cat_turno=id_cat_turno


    def to_json(self):
        return {
        'id_cuenta': self.id_cuenta,   
        'id_cat_turno': self.id_cat_turno
        }