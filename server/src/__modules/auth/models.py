import uuid

from sqlmodel import Field, SQLModel, UniqueConstraint


class User(SQLModel, table=True):
    """
    User model.

    Attributes
    ----------
    __table_args__ : tuple
        Arguments of the table.
    id : uuid.UUID
        ID of the user.
    name : str
        Name of the user.
    email : str
        Email of the user.
    password : str
        Password of the user.
    """

    __table_args__ = (UniqueConstraint("email"),)
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    password: str
