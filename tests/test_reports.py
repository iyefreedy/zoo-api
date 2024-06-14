# tests/test_reports.py
import json


def test_animal_report(client):
    response = client.get('/api/reports/animals')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert type(data) == dict


def test_visitor_report(client):
    response = client.get('/api/reports/visitors')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert type(data) == dict


def test_revenue_report(client):
    response = client.get('/api/reports/revenue')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert type(data) == dict
