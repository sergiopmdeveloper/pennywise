from unittest.mock import patch

from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

from src.__base.utils import init_app, lifespan
from src.__modules.user.router import router as user_router


async def test_lifespan():
    """
    WHEN the lifespan context is called,
    THEN the function create_db_and_tables should be called.
    """

    # WHEN
    with patch("src.__base.utils.create_db_and_tables") as mock_create_db_and_tables:
        async with lifespan(None):
            pass

    # THEN
    mock_create_db_and_tables.assert_called_once()


def test_init_app():
    """
    WHEN the init_app function is called,
    THEN the app should be instantiated with the expected parameters.
    """

    # WHEN
    with patch("src.__base.utils.FastAPI") as mock_app:
        init_app()

    # THEN
    mock_app.assert_called_once_with(lifespan=lifespan)
    mock_app.return_value.include_router.assert_called_once_with(user_router)
    mock_app.return_value.add_middleware.assert_called_once_with(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def test_get_root_redirection(client: TestClient):
    """
    WHEN a GET request is made to the root endpoint,
    THEN the response should be a redirection to the /docs page.
    """

    # WHEN
    response = client.get("/")

    # THEN
    assert response.url.path == "/docs"
    assert response.history[0].status_code == 307
