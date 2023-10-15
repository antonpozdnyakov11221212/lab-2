from pydantic import BaseModel
from typing import List


class Title(BaseModel):
    titles: List[str]


class Query(BaseModel):
    name: str
    content: str


class Info(BaseModel):
    name: str
    snt_cnt: int