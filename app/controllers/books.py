from starlite import get

from app.domain import books


@get("/books")
def get_books() -> books.Model:
    """Get books."""
    return books.Model(name="IT", genre="Horror")
