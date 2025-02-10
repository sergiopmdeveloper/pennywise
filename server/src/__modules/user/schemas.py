from pydantic import BaseModel, EmailStr, SecretStr

from src.__base.schemas import MutationResponseSchema
from src.__modules.auth.schemas import TokenSchema


class UserCreationSchema(BaseModel):
    """
    User creation schema.

    Attributes
    ----------
    name : str
        The name of the new user.
    email : EmailStr
        The email of the new user.
    password : SecretStr
        The password of the new user.
    """

    name: str
    email: EmailStr
    password: SecretStr


class CreatedUserSchema(MutationResponseSchema):
    """
    Created user schema.
    """

    token: TokenSchema
