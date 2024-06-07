import json
import os


class EmployeeRepository:
    def __init__(self) -> None:
        path = os.path.join(os.path.dirname(
            __file__), '../data/employees.json')
        self.filepath = path
        self.employees = self.load_employees()

    def load_employees(self):
        try:
            with open(self.filepath,  'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_employee(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.employees, file, indent=4)

    def get_all(self):
        return self.employees

    def get_by_id(self, employee_id):
        return next((employee for employee in self.employees if employee['id'] == employee_id), None)

    def add(self, new_employee):
        self.employees.append(new_employee)
        self.save_employee()

    def update(self, employee_id, data):
        employee = self.get_by_id(employee_id)
        if employee is not None:
            employee.update(data)
            self.save_employee()
            return employee
        return None

    def delete(self, employee_id):
        self.employees = [
            animal for animal in self.employees if animal['id'] != employee_id]
        self.save_employee()
