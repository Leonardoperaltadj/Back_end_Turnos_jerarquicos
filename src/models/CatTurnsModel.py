from database.db import db
from .entities.CatTurns import CatTurns
class CatTurnsModel():    
       
    @classmethod
    def registry(self, account):
        try:
            db.session.add(account)
            db.session.commit()
            
            return account
            
        except Exception as ex:   
            raise Exception(ex) 
        
    @classmethod
    def classification_turns(self, idTypeAccount):
        try:
           if idTypeAccount == 1:
            return 1
           if idTypeAccount == 2:
            return 2
           if idTypeAccount == 3:
            return 2
            
        except Exception as ex:   
            raise Exception(ex)    
        
    @classmethod    
    def get_cat_turns(self, id):    
        try: 
            id_cat_turns = CatTurns.query.get_or_404(id) 
            if id_cat_turns != None:
                cat_turns=CatTurns(id_cat_turns.id_cat_turno, id_cat_turns.turno)
                #account_json=account.to_json()
            return cat_turns
        except Exception as ex:   
            raise Exception(ex)          