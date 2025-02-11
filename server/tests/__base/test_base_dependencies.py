from unittest.mock import patch

from src.__base.dependencies import get_session


def test_get_session():
    """
    WHEN the get_session function is called,
    THEN a Session instance is created.
    """

    # WHEN
    with (
        patch("src.__base.dependencies.Session") as mock_session,
        patch("src.__base.dependencies.engine"),
    ):
        session_generator = get_session()
        next(session_generator)

    # THEN
    mock_session.assert_called_once()
