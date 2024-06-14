
import json


def test_get_feedings(client):
    response = client.get('/api/feedings/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert type(data['data']) == list


def test_add_feeding(client):
    new_feeding = {
        "animal_id": "1",
        "enclosure_id": "1",
        "food_type": "Meat",
        "feeding_time": "2024-06-13T10:00:00"
    }
    response = client.post(
        '/api/feedings/', data=json.dumps(new_feeding), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['data']['food_type'] == new_feeding['food_type']


def test_get_feeding(client):
    response = client.get('/api/feedings/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert type(data['data']) == dict


def test_update_feeding(client):
    updated_feeding = {
        "animal_id": "2",
        "enclosure_id": "2",
        "food_type": "Vegetables",
        "feeding_time": "2024-06-14T12:00:00"
    }
    response = client.put(
        '/api/feedings/1', data=json.dumps(updated_feeding), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['data']['food_type'] == updated_feeding['food_type']


def test_delete_feeding(client):
    response = client.delete('/api/feedings/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Feeding schedule deleted'
