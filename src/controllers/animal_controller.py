import os

from flask import Blueprint, jsonify, request
from flasgger import swag_from
from src.repositories.animal_repository import AnimalRepository

animals_blueprint = Blueprint('animals', __name__)
animal_repo = AnimalRepository()


@animals_blueprint.get('/')
@swag_from('../docs/list_animals.yml')
def get_animals():
    animals = animal_repo.get_all()
    return jsonify({'data': animals}), 200


@animals_blueprint.get('/<int:id>')
@swag_from('../docs/get_animal.yml')
def get_animals_by_id(id):
    animal = animal_repo.get_by_id(id)
    return jsonify({'data': animal}), 200


@animals_blueprint.post('/')
@swag_from('../docs/create_animal.yml')
def create_animal():
    new_animal = request.json
    if not all(key in new_animal for key in ('id', 'name', 'species', 'age')):
        return jsonify({'error': 'Missing data'}), 400
    animal_repo.add(new_animal)
    return jsonify({"message": "Animal created", "data": new_animal})


@animals_blueprint.put('/<int:id>')
@swag_from('../docs/edit_animal.yml')
def update_animal(id):
    data = request.json
    if not all(key in data for key in ('name', 'species', 'age')):
        return jsonify({'error': 'Missing data'}), 400
    animal = animal_repo.update(id, data)
    if animal is None:
        return jsonify({'error': 'Animal not found'}), 404
    return jsonify({"message": "Animal updated", "data": animal})


@animals_blueprint.delete('/<int:id>')
@swag_from('../docs/delete_animal.yml')
def delete_animal(id):
    animal_repo.delete(id)
    return '', 204
