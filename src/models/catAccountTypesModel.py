from database.db import db
from .entities.CatAccountTypes import CatAccountTypes
class CatAccountTypesModel():    
       
    @classmethod
    def registry(self, account):
        try:
            db.session.add(account)
            db.session.commit()
            
            return account
            
        except Exception as ex:   
            raise Exception(ex) 
        
    def get_cat_type_account(self, id):    
        try: 
            id_cat_account = CatAccountTypes.query.get_or_404(id) 
            if id_cat_account != None:
                cat_type_account=CatAccountTypes(id_cat_account.id_cat_tipo_cuenta, id_cat_account.cuenta)
                #account_json=account.to_json()
            return cat_type_account
        except Exception as ex:   
            raise Exception(ex)           