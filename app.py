from http import HTTPStatus

from fastapi import FastAPI

from schemas import LivroDB, LivroPublic, LivroSchema

app = FastAPI()

database = []


@app.get('/')
def read_root():
    return {'message': 'Hello World'}


@app.post(
    '/livros/',
    status_code=HTTPStatus.CREATED,
    response_model=LivroPublic,
)
def create_livro(livro: LivroSchema):
    livro_com_id = LivroDB(
        **livro.model_dump(),
        id=len(database) + 1,
    )

    database.append(livro_com_id)

    return livro_com_id


@app.get('/livros/', response_model=list[LivroPublic])
def read_livros():
    return database