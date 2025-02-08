from fastapi.responses import RedirectResponse

from src.__base.utils import init_app

app = init_app()


@app.get("/")
async def root() -> RedirectResponse:
    """
    GET | / | Redirects to the /docs endpoint.

    Returns
    -------
    RedirectResponse
        The redirection.
    """

    return RedirectResponse(url="/docs")
