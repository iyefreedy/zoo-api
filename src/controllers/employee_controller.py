
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from src.repositories.employee_repository import EmployeeRepository

employee_blueprint = Blueprint('employees', __name__, url_prefix='/employees')
employee_repo = EmployeeRepository()


@employee_blueprint.get('/')
@swag_from('../docs/employee/list_employees.yml')
def get_employees():
    employees = employee_repo.get_all()
    return jsonify({'data': employees}), 200


@employee_blueprint.get('/<int:id>')
@swag_from('../docs/employee/get_employee.yml')
def get_employee(id):
    employee = employee_repo.get_by_id(id)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({'data': employee}), 200


@employee_blueprint.post('/')
@swag_from('../docs/employee/create_employee.yml')
def create_employee():
    new_employee = request.json
    if not all(key in new_employee for key in ('name', 'email', 'phone_number', 'role', 'schedule')):
        return jsonify({'error': 'Missing parameter'}), 400
    employee_repo.add(new_employee)
    return jsonify({"message": "Employee created", "data": new_employee}), 201


@employee_blueprint.put('/<int:id>')
@swag_from('../docs/employee/edit_employee.yml')
def update_employee(id):
    new_employee = request.json
    if not all(key in new_employee for key in ('name', 'email', 'phone_number', 'role', 'schedule')):
        return jsonify({'error': 'Missing parameter'}), 400
    employee = employee_repo.update(id, new_employee)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({"message": "Employee updated", "data": employee})


@employee_blueprint.delete('/<int:id>')
@swag_from('../docs/employee/delete_employee.yml')
def delete_employee(id):
    employee_repo.delete(id)
    return jsonify({"message": "Employee deleted"}), 200
