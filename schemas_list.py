from typing import List, Union

from pydantic import BaseModel


class List_kantin_Base(BaseModel):
    id: int
    nama: str
    lokasi: str


class List_kantin_Create(List_kantin_Base):
    pass

    class Config:
        orm_mode = True

class List_kantin_get(List_kantin_Base):
    id: int

    class Config:
        orm_mode = True