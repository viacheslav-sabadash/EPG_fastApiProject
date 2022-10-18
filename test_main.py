from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello world"


def test_read_index():
    response = client.get("/index")
    assert response.status_code == 200
    assert response.text == "Hello world"


def test_eval():
    response = client.get("/eval?phrase=(3+6)/2")
    assert response.status_code == 200
    assert response.text == '(3+6)/2 = 4.5'


def test_eval_division_by_zero():
    response = client.get("/eval?phrase=(3+6)/0")
    assert response.status_code == 400
    assert response.text == 'Error: division by zero'


def test_eval_post():
    response = client.post(
        "/eval",
        headers={"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
        data="phrase=3%2B3*2"
    )
    assert response.status_code == 201
    assert response.json() == {'data': {'phrase': '3+3*2', 'value': 9}}


def test_eval_post_invalid_syntax():
    response = client.post(
        "/eval",
        headers={"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
        data="phrase=3+++3"
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Error: invalid syntax'}
