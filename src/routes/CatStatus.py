from flask import Blueprint, jsonify

# Models
from models.CatStatusModel import CatStatusModel
from models.entities.CatStatus import CatStatus
estatus = Blueprint('estatus', __name__,)

@estatus.route('/',)
def get_estatus():
    try:
        estatus = CatStatus.query.all()
        results = [
            {
                "id_cat_estatus": status.id_cat_estatus,
                "estatus": status.estatus
                
            } for status in estatus]

        return {"CatEstatus": results}
    except Exception as ex:
        return jsonify({'message': str(ex)}),500