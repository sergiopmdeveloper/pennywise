from unittest.mock import patch

import jwt
import pytest

from src.__modules.auth.utils import JWTHandler


def test_jwt_handler_generate_token(monkeypatch):
    """
    WHEN the JWTHandler.generate_token function is called,
    THEN a new token is generated.
    """

    monkeypatch.setenv("SECRET_KEY", "secret")

    # WHEN
    token = JWTHandler.generate_token(data={"key": "value"})

    # THEN
    assert isinstance(token, str)


def test_jwt_handler_validate_token_jwt_error():
    """
    WHEN the JWTHandler.validate_token function is called with an invalid token,
    THEN a jwt.PyJWTError exception is raised with an error message.
    """

    # WHEN
    with pytest.raises(jwt.PyJWTError) as e:
        JWTHandler.validate_token(token="invalid_token")

    # THEN
    assert e.value.args[0] == "Invalid token"


def test_jwt_handler_validate_token_unknown_error():
    """
    WHEN the JWTHandler.validate_token function is called and an unexpected error occurs,
    THEN a generic exception is raised with an error message.
    """

    # WHEN
    with patch("src.__modules.auth.utils.jwt.decode") as mock_decode:
        mock_decode.side_effect = Exception()
        with pytest.raises(Exception) as e:
            JWTHandler.validate_token(token="buggy_token")

    # THEN
    assert e.value.args[0] == "Unknown error"


def test_jwt_handler_validate_token_success(monkeypatch):
    """
    WHEN the JWTHandler.validate_token function is called with a valid token,
    THEN the token data is returned.
    """

    monkeypatch.setenv("SECRET_KEY", "secret")

    # WHEN
    token = JWTHandler.generate_token(data={"key": "value"})
    data = JWTHandler.validate_token(token=token)
    data.pop("exp")

    # THEN
    assert data == {"key": "value"}
