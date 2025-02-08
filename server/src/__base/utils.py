from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.__base.constants import ALLOWED_ORIGINS
from src.__database.utils import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """
    App lifetime context manager. Executes the following steps:

    On startup:
    - Initialise the database and its corresponding tables if necessary.

    Parameters
    ----------
    _ : FastAPI
        The app instance, not used.
    """

    create_db_and_tables()

    yield


def init_app() -> FastAPI:
    """
    Initialises the app.

    Returns
    -------
    FastAPI
        The initialised app.
    """

    app = FastAPI(lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
