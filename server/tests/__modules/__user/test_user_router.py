from fastapi.testclient import TestClient
from sqlmodel import Session

from src.__modules.user.models import User


def test_post_user_success(monkeypatch, client):
    """
    WHEN a valid POST request is made to the user endpoint,
    THEN the response returns 201 with the created entity details.
    """

    monkeypatch.setenv("SECRET_KEY", "secret")

    # WHEN
    response = client.post(
        "/user",
        json={
            "name": "name",
            "email": "test@email.com",
            "password": "password",
        },
    )
    data = response.json()

    # THEN
    assert response.status_code == 201
    assert data["entity"] == "user"
    assert data["action"] == "create"
    assert data.get("affected_ids")


def test_post_user_conflict(session, client):
    """
    GIVEN an existing user,
    WHEN a POST request is made to the user endpoint with the same email as the existing one,
    THEN the response returns 409 with a conflict message.
    """

    # GIVEN
    user = User(
        name="name",
        email="test@email.com",
        password="password",
    )
    session.add(user)
    session.commit()

    # WHEN
    response = client.post(
        "/user",
        json={
            "name": "name",
            "email": "test@email.com",
            "password": "password",
        },
    )
    data = response.json()

    # THEN
    assert response.status_code == 409
    assert data["detail"] == "Email already exists"
