from database.db import db
from .entities.Turns import Turns
from models.AccountsModel import AccountsModel
from models.CatTurnsModel import CatTurnsModel

class TurnsModel():    
       
    @classmethod
    def registry(self, turn):
        try:
            db.session.add(turn)
            db.session.commit()
            
            return turn
            
        except Exception as ex:   
            raise Exception(ex) 
        
    @classmethod
    def get_turn(self, id):
        try:
            id_turn = Turns.query.filter_by(id_cuenta=int(id)).first() 
            if id_turn != None:
                turn=Turns(id_turn.id_cuenta, id_turn.id_cat_turno)
                #account_json=account.to_json()
            
            return turn
            
        except Exception as ex:   
            raise Exception(ex)         
 
    @classmethod    
    def get_account_turn(self):    
        try: 
            results_turn=[]
            results_accounts=[]
            result_cat_turns=[]
            turns=Turns.query.all()
            for turn in turns:
                data_turn=Turns(turn.id_cuenta, turn.id_cat_turno)
                results_turn.append(data_turn.to_json())
                data_account=AccountsModel.get_account(turn.id_cuenta)
                results_accounts.append(data_account.to_json())
                data_cat_turns=CatTurnsModel.get_cat_turns(turn.id_cat_turno)
                result_cat_turns.append(data_cat_turns.to_json())
                
                
            return results_turn,results_accounts ,result_cat_turns
        except Exception as ex:   
            raise Exception(ex)         
        
        