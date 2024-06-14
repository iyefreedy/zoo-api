from flask import request, Blueprint, jsonify
from flasgger import swag_from
from src.repositories.enclosure_repository import EnclosureRepository

enclosure_blueprint = Blueprint(
    'enclosures', __name__, url_prefix='/enclosures')
enclosure_repo = EnclosureRepository()


@enclosure_blueprint.get('/')
@swag_from('../docs/enclosure/list_enclosures.yml')
def get_enclosures():
    enclosures = enclosure_repo.get_all()
    return jsonify({"data": enclosures}), 200


@enclosure_blueprint.get('/<int:id>')
@swag_from('../docs/enclosure/get_enclosure.yml')
def get_enclosure(id):
    enclosure = enclosure_repo.get_by_id(id)
    if enclosure is None:
        return jsonify({"data": "Enclosure not found"}), 404
    return jsonify({"data": enclosure}), 200


@enclosure_blueprint.post('/')
@swag_from('../docs/enclosure/create_enclosure.yml')
def create_enclosure():
    new_enclosure = request.json
    if not all(key in new_enclosure for key in ('name', 'description')):
        return jsonify({'error': 'Missing parameter'}), 400
    enclosure_repo.add(new_enclosure)
    return jsonify({"message": "Enclosure created", "data": new_enclosure}), 201


@enclosure_blueprint.put('/<int:id>')
@swag_from('../docs/enclosure/edit_enclosure.yml')
def update_enclosure(id):
    data = request.json
    updated_enclosure = enclosure_repo.update(id, data)
    if updated_enclosure is None:
        return jsonify({'error': "Enclosure not found"}), 404
    return jsonify({'message': "Enclosure updated", "data": updated_enclosure})


@enclosure_blueprint.delete('/<int:id>')
@swag_from('../docs/enclosure/delete_enclosure.yml')
def delete_enclosure(id):
    enclosure_repo.delete(id)
    return jsonify({"message": "Enclosure deleted"}), 200
