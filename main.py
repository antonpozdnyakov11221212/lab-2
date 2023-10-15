from fastapi import FastAPI
from models import *
import wikipedia


app = FastAPI()


@app.get("/{name}", response_model=Title)
def with_path(name: str):
    return Title(titles=wikipedia.search(name))


@app.get("/query/{title}", response_model=Query)
def with_query(title: str, snt_cnt: int):
    return Query(name=title, content=wikipedia.summary(title, sentences=snt_cnt))


@app.post("/", response_model=Query)
def with_class(full_info: Info):
    return Query(name=full_info.name, content=wikipedia.summary(full_info.name, sentences=full_info.snt_cnt))