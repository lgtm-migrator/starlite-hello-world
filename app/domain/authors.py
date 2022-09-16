from pydantic import BaseModel


class Model(BaseModel):
    """Author model."""

    name: str
    dead: bool
