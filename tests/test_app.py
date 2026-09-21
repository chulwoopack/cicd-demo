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
    assert b"Hello World!" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
