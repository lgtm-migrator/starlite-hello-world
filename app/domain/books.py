from pydantic import BaseModel


class Model(BaseModel):
    """Book model."""

    name: str
    genre: str
