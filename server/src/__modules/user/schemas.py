from pydantic import BaseModel, EmailStr, SecretStr


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
