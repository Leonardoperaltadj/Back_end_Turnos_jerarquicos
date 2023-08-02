from database.db import db

class TurnsModel():    
       
    @classmethod
    def registry(self, turn):
        try:
            db.session.add(turn)
            db.session.commit()
            
            return turn
            
        except Exception as ex:   
            raise Exception(ex) 