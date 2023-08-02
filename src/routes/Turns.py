from flask import Blueprint, jsonify, request
#entities
from models.entities.Turns import Turns
# Models
from models.TurnsModel import TurnsModel
#blueprint
Turn = Blueprint('Turns', __name__,)

@Turn.route('/registry', methods=['POST'])
def registryTurns():
    try:
        idCatTurn = request.json['id_cat_turno']
        id_account = request.json['id_account']     

        turn = Turns(idCatTurn, id_account)
        TurnsModel.registry(turn)
       
        return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 