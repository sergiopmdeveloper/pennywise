import os
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from argon2 import PasswordHasher

password_hasher = PasswordHasher()


class JWTHandler:
    """
    JWT handler.

    Attributes
    ----------
    __ALGORITHM : str
        The algorithm to be used to generate the token.
    __ACCESS_TOKEN_EXPIRE_MINUTES : int
        The number of minutes the token is valid for.

    Methods
    -------
    generate_token(data: dict[str, Any]) -> str
        Generates a token.
    validate_token(token: str) -> dict[str, Any]
        Validates the token and returns the decoded data.
    """

    __ALGORITHM = "HS256"
    __ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

    @classmethod
    def generate_token(cls, data: dict[str, Any]) -> str:
        """
        Generates a token.

        Parameters
        ----------
        data : dict[str, Any]
            The data to encode in the token.

        Returns
        -------
        str
            The generated token.
        """

        data_copy = data.copy()

        expire_date = datetime.now(timezone.utc) + timedelta(
            minutes=cls.__ACCESS_TOKEN_EXPIRE_MINUTES
        )

        data_copy["exp"] = expire_date

        token = jwt.encode(
            data_copy,
            os.getenv("SECRET_KEY"),
            algorithm=cls.__ALGORITHM,
        )

        return token

    @classmethod
    def validate_token(cls, token: str) -> dict[str, Any]:
        """
        Validates the token and returns the decoded data.

        Parameters
        ----------
        token : str
            The token to validate.

        Returns
        -------
        dict[str, Any]
            The decoded data.

        Raises
        ------
        jwt.PyJWTError
            If the token is invalid.
        Exception
            If an unexpected error occurs.
        """

        try:
            return jwt.decode(
                token, os.getenv("SECRET_KEY"), algorithms=[cls.__ALGORITHM]
            )
        except jwt.PyJWTError:
            raise jwt.PyJWTError("Invalid token")
        except Exception as e:
            raise e
