from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from sqlalchemy.orm import Session

import models_list, schemas_list
from models_list import List_kantin

async def create_list(list_kantin: schemas_list.List_kantin_Create, db:Session) -> schemas_list.List_kantin_get:
    db_list = models_list.List_kantin(id=list_kantin.id, nama=list_kantin.nama, lokasi=list_kantin.lokasi)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

async def get_all_list(db: Session) -> List[schemas_list.List_kantin_get]:
    list_kantin = db.query(models_list.List_kantin).order_by(models_list.List_kantin.id.desc()).all()
    if list_kantin is None:
        return {"Details": "Tidak ada kantin yang tersedia"}
    return list(map(schemas_list.List_kantin_get.from_orm, list_kantin))