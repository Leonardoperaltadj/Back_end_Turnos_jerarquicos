from flask import Blueprint, jsonify, request
#entities
from models.entities.CatTurns import CatTurns
# Models
from models.CatTurnsModel import CatTurnsModel
#blueprint
CatTurn = Blueprint('CatTurns', __name__,)

@CatTurn.route('/registry', methods=['POST'])
def registryTypeTurns():
    try:
        idCatTurn = request.json['id_cat_turno']
        turn = request.json['turno']     

        cat_turn = CatTurns(idCatTurn, turn)
        CatTurnsModel.registry(cat_turn)
       
        return {"status":200}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 