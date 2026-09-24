import pytest

from cicd_demo.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_homepage_returns_hello_world(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello CI/CD!" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_greet_with_name(client):
    response = client.get("/greet?name=Alice")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alice!"}


def test_greet_without_name(client):
    response = client.get("/greet")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Guest!"}
