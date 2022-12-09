from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from sqlalchemy.orm import Session

import models_menu, schemas_menu
from models_menu import Menu_kantin

async def create_menu(menu_kantin: schemas_menu.Menu_kantin_Create, db:Session) -> schemas_menu.Menu_kantin_get:
    db_menu = models_menu.Menu_kantin(id_kantin=menu_kantin.id_kantin, id_menu=menu_kantin.id_menu, nama_menu=menu_kantin.nama_menu, harga_menu=menu_kantin.harga_menu, ketersediaan=menu_kantin.ketersediaan)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

async def get_all_menu(db: Session) -> List[schemas_menu.Menu_kantin_get]:
    menu_kantin = db.query(models_menu.Menu_kantin).all()
    if menu_kantin is None:
        return {"Details": "Tidak ada menu yang tersedia"}
    return list(map(schemas_menu.Menu_kantin_get.from_orm, menu_kantin))

async def get_menu_kantin(id_kantin: int, db: Session) -> List[schemas_menu.Menu_kantin_get]:
    menu_kantin = db.query(models_menu.Menu_kantin).filter(models_menu.Menu_kantin.id_kantin == id_kantin).all()
    print(menu_kantin)
    if menu_kantin is None:
        return {"Details": "Tidak ada menu yang tersedia"}
    return list(map(schemas_menu.Menu_kantin_get.from_orm, menu_kantin))

async def update_ketersediaan(id_kantin: int, id_menu: int, ketersediaan: str, db: Session) -> schemas_menu.Menu_kantin_Base:
    cek_ketersediaan = db.query(models_menu.Menu_kantin).filter(models_menu.Menu_kantin.id_kantin == id_kantin, models_menu.Menu_kantin.id_menu == id_menu).all()
    if cek_ketersediaan == []:
        raise HTTPException(status_code=400, detail="Menu Invalid")
    update_ketersediaan = db.query(models_menu.Menu_kantin).filter(models_menu.Menu_kantin.id_kantin == id_kantin, models_menu.Menu_kantin.id_menu == id_menu, models_menu.Menu_kantin.ketersediaan == ketersediaan).update({models_menu.Menu_kantin.ketersediaan: ketersediaan})
    db.commit()
    return {"status": "Ketersediaan Berhasil Diubah"}

async def get_pendapatan(id_kantin: int, keramaian: int, db: Session):
    cek_kantin = db.query(models_menu.Menu_kantin).filter(models_menu.Menu_kantin.id_kantin==id_kantin).all()
    if cek_kantin == []:
        raise HTTPException(status_code=400, detail="Kantin Invalid")
    pendapatan = db.query(func.avg(models_menu.Menu_kantin.harga_menu)).where(models_menu.Menu_kantin.id_kantin==id_kantin, models_menu.Menu_kantin.ketersediaan=="ada").all()
    intPendapatan = pendapatan[0][0]
    totalPendapatan = keramaian * intPendapatan
    return totalPendapatan