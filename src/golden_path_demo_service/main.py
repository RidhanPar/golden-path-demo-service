"""Golden Path Demo Service: HTTP entry point."""

from fastapi import FastAPI
from pydantic import BaseModel

from golden_path_demo_service import __version__

app = FastAPI(title="Golden Path Demo Service", version=__version__)


class Health(BaseModel):
    status: str
    version: str


class Greeting(BaseModel):
    message: str


@app.get("/health")
def health() -> Health:
    """Liveness probe used by Docker HEALTHCHECK and the deploy platform."""
    return Health(status="ok", version=__version__)


@app.get("/hello")
def hello(name: str = "world") -> Greeting:
    """Return a greeting for ``name``."""
    return Greeting(message=f"Hello, {name}!")


def shout(name: str) -> str:
    """Upper-case greeting."""
    return hello(name).message.upper
