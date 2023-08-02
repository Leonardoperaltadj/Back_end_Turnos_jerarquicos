from database.db import db

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