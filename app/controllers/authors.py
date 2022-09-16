from starlite import get

from app.domain import authors


@get("/authors")
def get_authors() -> authors.Model:
    """Get authors."""
    return authors.Model(name="Stephen King", dead=False)
