from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    name: str
    last_name: str
    email: str
    password: str
    bday: str
    sex: str
    interests: list[str]
    city: str


