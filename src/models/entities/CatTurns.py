from database.db import db

class CatTurns(db.Model):
    __tablename__ = 'cat_turno'

    id_cat_turno = db.Column(db.SmallInteger, primary_key=True)
    turno = db.Column(db.String(20), nullable=False)
    turns = db.relationship('Turns', backref='cat_turno', lazy = True )

    def __init__(self, id_cat_turno, turno=None):
        self.id_cat_turno=id_cat_turno
        self.turno=turno


    def to_json(self):
        return {
        'id_cat_turno': self.id_cat_turno,   
        'turno': self.turno
        }