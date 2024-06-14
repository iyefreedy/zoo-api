from flask import request, Blueprint, jsonify
from flasgger import swag_from
from src.repositories.feeding_repository import FeedingRepository

feeding_blueprint = Blueprint('feedings', __name__, url_prefix='/feedings')
feeding_repo = FeedingRepository()


@feeding_blueprint.get('/')
@swag_from('../docs/feeding/list_feedings.yml')
def get_feedings():
    feedings = feeding_repo.get_all()
    return jsonify({"data": feedings}), 200


@feeding_blueprint.get('/<int:id>')
@swag_from('../docs/feeding/get_feeding.yml')
def get_feeding(id):
    feeding = feeding_repo.get_by_id(id)
    if feeding is None:
        return jsonify({"error": "Feeding schedule not found"})
    return jsonify({"data": feeding}), 200


@feeding_blueprint.post('/')
@swag_from('../docs/feeding/create_feeding.yml')
def create_feeding():
    new_feeding_schedule = request.get_json()
    if not all(key in new_feeding_schedule for key in ('animal_id', 'enclosure_id', 'feeding_time', 'food_type')):
        return jsonify({"error": "Missing parameter"}), 400
    feeding_repo.add(new_feeding_schedule)
    return jsonify({"message": "Feeding schedule created", "data": new_feeding_schedule}), 201


@feeding_blueprint.put('/<int:id>')
@swag_from('../docs/feeding/edit_feeding.yml')
def update_feeding(id):
    data = request.get_json()
    if not all(key in data for key in ('animal_id', 'enclosure_id', 'feeding_time', 'food_type')):
        return jsonify({"error": "Missing parameter"})
    updated_feeding_schedule = feeding_repo.update(id, data)
    if updated_feeding_schedule is None:
        return jsonify({"error": "Feeding schedule not found"})
    feeding_repo.update(id, updated_feeding_schedule)
    return jsonify({"message": "Feeding schedule updated", 'data': updated_feeding_schedule})


@feeding_blueprint.delete('/<int:id>')
@swag_from('../docs/feeding/delete_feeding.yml')
def delete_feeding(id):
    feeding_repo.delete(id)
    return jsonify({"message": "Feeding schedule deleted"}), 200
