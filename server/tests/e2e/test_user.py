from fastapi.testclient import TestClient
from sqlmodel import Session

from src.__modules.user.models import User


def test_post_user_success(client: TestClient):
    """
    WHEN a POST request is made to create a new user,
    THEN the response should return a 201 status code with the details of the mutation.
    """

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


def test_post_user_conflict(session: Session, client: TestClient):
    """
    GIVEN an existing user in the database,
    WHEN a POST request is made to create a new user with the same email,
    THEN the response should return a 409 status code with a message indicating that the email already exists.
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
