from starlite import Starlite

from .controllers import authors, books

app = Starlite(route_handlers=[authors.get_authors, books.get_books])
