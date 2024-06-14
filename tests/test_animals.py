import json


def test_get_animals(client):
    response = client.get('/api/animals/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert type(data['data']) == list


def test_add_animal(client):
    new_animal = {
        "species": "Tiger",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Large enclosure"
    }
    response = client.post(
        '/api/animals/', data=json.dumps(new_animal), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'data' in data
    assert type(data['data']) == dict


def test_get_animal(client):
    response = client.get('/api/animals/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data


def test_update_animal(client):
    updated_animal = {
        "species": "Updated Species",
        "age": 4,
        "gender": "Female",
        "special_requirements": "Updated requirements"
    }
    response = client.put(
        '/api/animals/1', data=json.dumps(updated_animal), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data


def test_delete_animal(client):
    response = client.delete('/api/animals/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Animal deleted'
