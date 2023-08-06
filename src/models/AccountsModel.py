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
                account=Accounts(data_account.id_cuenta,data_account.nombre, data_account.correo, Accounts.check_password(data_account.contrasena, account.contrasena),data_account.id_cat_tipo_cuenta)
                return account
            else:
                return None        
        except Exception as ex:   
            raise Exception(ex)   
        
    @classmethod    
    def get_by_id(self, id):    
        try: 
            id_account = Accounts.query.get_or_404(id) 
            account=None
            if id_account != None:
                account=Accounts(id_account.id_cuenta,id_account.nombre, id_account.correo, id_account.contrasena, id_account.id_cat_tipo_cuenta)
                #account=account.to_json()

            return account
        except Exception as ex:   
            raise Exception(ex)   
        
    @classmethod    
    def get_account(self, id):    
        try: 
            id_account = Accounts.query.get_or_404(id) 
            if id_account != None:
                account=Accounts(id_account.id_cuenta,id_account.nombre, id_account.correo, id_account.contrasena, id_account.id_cat_tipo_cuenta)
                #account_json=account.to_json()
            return account
        except Exception as ex:   
            raise Exception(ex)  
        
       
        
        
              
        
               