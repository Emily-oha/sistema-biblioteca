from pydantic import BaseModel


class LivroSchema(BaseModel):
    titulo: str
    autor: str
    ano: int
    isbn: str


class LivroPublic(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    isbn: str


class LivroDB(LivroSchema):
    id: int