from sqlmodel import SQLModel, create_engine

from src.__database.constants import CONNECT_ARGS, DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args=CONNECT_ARGS)


def create_db_and_tables() -> None:
    """
    Initialise the database and its corresponding tables if necessary.
    """

    __import__("src.__modules.user.models")

    SQLModel.metadata.create_all(engine)
