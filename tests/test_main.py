from starlite.testing import TestClient

from main import app


def test_app() -> None:
    with TestClient(app=app) as client:
        assert client.post("/", json={"a": "a", "b": 1}).json() == {"a": "a", "b": 1}
