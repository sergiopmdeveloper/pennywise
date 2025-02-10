from pydantic import BaseModel


class TokenSchema(BaseModel):
    """
    Token schema.

    Attributes
    ----------
    value : str
        The value of the token.
    type : str
        The type of the token, by default "bearer".
    """

    value: str
    type: str = "bearer"
