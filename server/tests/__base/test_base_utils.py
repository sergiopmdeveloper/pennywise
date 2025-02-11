from unittest.mock import patch

from fastapi.middleware.cors import CORSMiddleware

from src.__base.utils import init_app, lifespan
from src.__modules.user.router import router as user_router


async def test_lifespan():
    """
    WHEN the lifespan context is entered,
    THEN the create_db_and_tables function is called.
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
    THEN a FastAPI instance is created with the expected parameters.
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
