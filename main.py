"""Minimal Starlite application."""
from typing import TypedDict

from starlite import Starlite, post

from typeddict_plugin import TypedDictPlugin


class DataType(TypedDict):
    """A typed dict."""

    a: str
    b: int


@post("/")
def hello_world(data: DataType) -> DataType:
    """Route Handler that outputs hello world."""
    return data


app = Starlite(route_handlers=[hello_world], plugins=[TypedDictPlugin()])
