# tests/test_employees.py
import json


def test_get_employees(client):
    response = client.get('/api/employees/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert type(data['data']) == list


def test_add_employee(client):
    new_employee = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone_number": "123-456-7890",
        "role": "Zookeeper",
        "schedule": "Mon-Fri"
    }
    response = client.post(
        '/api/employees/', data=json.dumps(new_employee), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Employee created'
    assert 'data' in data
    assert type(data['data']) == dict


def test_get_employee(client):
    response = client.get('/api/employees/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert data['data']['id'] == 1


def test_update_employee(client):
    updated_employee = {
        "name": "Updated Name",
        "email": "updated.email@example.com",
        "phone_number": "987-654-3210",
        "role": "Manager",
        "schedule": "Mon-Fri"
    }
    response = client.put(
        '/api/employees/1', data=json.dumps(updated_employee), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == 'Employee updated'
    assert 'data' in data
    assert data['data']['name'] == updated_employee['name']


def test_delete_employee(client):
    response = client.delete('/api/employees/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Employee deleted'
