from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.__base.constants import ALLOWED_ORIGINS


def init_app() -> FastAPI:
    """
    Initialises the app.

    Returns
    -------
    FastAPI
        The initialised app.
    """

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
