from fastapi.testclient import TestClient


def test_get_root_redirection(client):
    """
    WHEN a GET request is made to the root endpoint,
    THEN the response returns 307 with a redirection to the docs endpoint.
    """

    # WHEN
    response = client.get("/")

    # THEN
    assert response.url.path == "/docs"
    assert response.history[0].status_code == 307
