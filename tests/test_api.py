import pytest

from api import create_app
from flask import request, jsonify

#Command py -m pytest tests
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            yield client

app = create_app()

def test_api():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'test'
    })
    data = response.get_json()
    assert data['result'] == 'sanitized'

# BAD
def test_api2():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'; DROP table;'
    })
    data = response.get_json()
    assert data['result'] == 'unsanitized'

#BAD
def test_api3():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'     SELECT FROM * PASSWORD;'
    })
    data = response.get_json()
    assert data['result'] == 'unsanitized'

def test_api4():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'good text no errors'
    })
    data = response.get_json()
    assert data['result'] == 'sanitized'

def test_api5():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'test           spaces'
    })
    data = response.get_json()
    assert data['result'] == 'sanitized'

#BAD
def test_api6():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'; no sql error here'
    })
    data = response.get_json()
    assert data['result'] == 'sanitized'
#BAD
def test_api7():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'DELETE * from users;'
    })
    data = response.get_json()
    assert data['result'] == 'unsanitized'

#BAD
def test_api8():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'; DROP all items'
    })
    data = response.get_json()
    assert data['result'] == 'unsanitized'

def test_api9():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'a string of good words...'
    })
    data = response.get_json()
    assert data['result'] == 'sanitized'

#AD
def test_api10():
    response = app.test_client().post(
        '/v1/sanitized/input', json={
            'payload':'test .234 random'
    })
    data = response.get_json()
    assert data['result'] == 'sanitized'
