from .entities.Accounts import Accounts
from database.db import db

class AccountsModel():    
       
    @classmethod
    def registry(self, account):
        try:
            db.session.add(account)
            db.session.commit()
            
            return account
            
        except Exception as ex:   
            raise Exception(ex) 