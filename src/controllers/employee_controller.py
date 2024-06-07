
import os

from flask import Blueprint, jsonify, request
from flasgger import swag_from
from src.repositories.employee_repository import EmployeeRepository

employee_blueprint = Blueprint('employees', __name__)
employee_repo = EmployeeRepository()


@employee_blueprint.get('/')
@swag_from('../docs/list_employees.yml')
def get_animals():
    employees = employee_repo.get_all()
    return jsonify({'data': employees}), 200


@employee_blueprint.get('/<int:id>')
@swag_from('../docs/get_employee.yml')
def get_animals_by_id(id):
    employee = employee_repo.get_by_id(id)
    if employee is None:
        return jsonify({'error': 'Employee not found'})
    return jsonify({'data': employee}), 200


@employee_blueprint.post('/')
@swag_from('../docs/create_employee.yml')
def create_animal():
    new_employee = request.json
    if not all(key in new_employee for key in ('id', 'name', 'email', 'phone_number', 'email', 'role', 'schedule')):
        return jsonify({'error': 'Missing parameter'}), 400
    employee_repo.add(new_employee)
    return jsonify({"message": "Employee created", "data": new_employee})


@employee_blueprint.put('/<int:id>')
@swag_from('../docs/edit_employee.yml')
def update_animal(id):
    data = request.json
    if not all(key in data for key in ('name', 'species', 'age')):
        return jsonify({'error': 'Missing data'}), 400
    animal = employee_repo.update(id, data)
    if animal is None:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({"message": "Animal updated", "data": animal})


@employee_blueprint.delete('/<int:id>')
@swag_from('../docs/delete_employee.yml')
def delete_animal(id):
    employee_repo.delete(id)
    return '', 204
