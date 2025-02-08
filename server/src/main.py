from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


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
