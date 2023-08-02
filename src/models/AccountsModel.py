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
        
    @classmethod    
    def login(self, account):    
        try: 
            data_account = Accounts.query.filter_by(correo=str(account.correo)).first()
            #print(data_account)
            if data_account != None:
                account=Accounts(data_account.nombre, data_account.correo, Accounts.check_password(data_account.contrasena, account.contrasena),data_account.id_cat_tipo_cuenta)
                return account
            else:
                return None        
        except Exception as ex:   
            raise Exception(ex)     