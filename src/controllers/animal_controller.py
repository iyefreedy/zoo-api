from flask import Blueprint, jsonify, request
from flasgger import swag_from
from src.repositories.animal_repository import AnimalRepository

animals_blueprint = Blueprint('animals', __name__, url_prefix='/animals')
animal_repo = AnimalRepository()


@animals_blueprint.get('/')
@swag_from('../docs/animal/list_animals.yml')
def get_animals():
    animals = animal_repo.get_all()
    return jsonify({'data': animals}), 200


@animals_blueprint.get('/<int:id>')
@swag_from('../docs/animal/get_animal.yml')
def get_animal(id):
    animal = animal_repo.get_by_id(id)
    if animal is None:
        return jsonify({"message": "Animal not found"}), 404
    return jsonify({'data': animal}), 200


@animals_blueprint.post('/')
@swag_from('../docs/animal/create_animal.yml')
def create_animal():
    new_animal = request.json
    if not all(key in new_animal for key in ('gender', 'species', 'age', 'special_requirements')):
        return jsonify({'error': 'Missing parameter'}), 400
    animal_repo.add(new_animal)
    return jsonify({"message": "Animal created", "data": new_animal}), 201


@animals_blueprint.put('/<int:id>')
@swag_from('../docs/animal/edit_animal.yml')
def update_animal(id):
    data = request.json
    if not all(key in data for key in ('gender', 'species', 'age', 'special_requirements')):
        return jsonify({'error': 'Missing parameters'}), 400
    animal = animal_repo.update(id, data)
    if animal is None:
        return jsonify({'error': 'Animal not found'}), 404
    return jsonify({"message": "Animal updated", "data": animal})


@animals_blueprint.delete('/<int:id>')
@swag_from('../docs/animal/delete_animal.yml')
def delete_animal(id):
    animal_repo.delete(id)
    return jsonify({"message": "Animal deleted"}), 200
