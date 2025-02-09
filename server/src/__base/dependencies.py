from typing import Generator

from sqlmodel import Session

from src.__database.utils import engine


def get_session() -> Generator[Session, None, None]:
    """
    Gets a database session.

    Yields
    ------
    Session
        The database session.
    """

    with Session(engine) as session:
        yield session
