from typing import List, Union

from pydantic import BaseModel

class Menu_kantin_Base(BaseModel):
    id_kantin: int
    id_menu: int
    nama_menu: str
    harga_menu: int
    ketersediaan: str


class Menu_kantin_Create(Menu_kantin_Base):
    pass

    class Config:
        orm_mode = True

class Menu_kantin_get(Menu_kantin_Base):
    id_kantin: int

    class Config:
        orm_mode = True