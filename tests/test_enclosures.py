import json


def test_get_enclosures(client):
    response = client.get('/api/enclosures/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert type(data['data']) == list


def test_get_enclosure(client):
    response = client.get('/api/enclosures/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert data['data']['id'] == 1


def test_add_enclosure(client):
    new_enclosure = {
        "name": "Elephant Enclosure",
        "description": "A spacious area with a pond and plenty of shade."
    }
    response = client.post(
        '/api/enclosures/', data=json.dumps(new_enclosure), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'data' in data
    assert data['data']['name'] == new_enclosure['name']


def test_update_enclosure(client):
    updated_enclosure = {
        "name": "Elephant Enclosure",
        "description": "A spacious area with a pond and plenty of shade."
    }
    response = client.put(
        '/api/enclosures/1', data=json.dumps(updated_enclosure), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert data['data']['name'] == updated_enclosure['name']


def test_delete_enclosure(client):
    response = client.delete('/api/enclosures/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Enclosure deleted'
