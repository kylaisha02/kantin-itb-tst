from typing import List
from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
import services_menu, schemas_menu, models_menu

app = FastAPI()
router = APIRouter(
	prefix='/menu_kantin',
	tags=['Menu_kantin']
)

models_menu.connection.Base.metadata.create_all(bind=connection.engine)

@router.post("/menu_kantin", response_model=schemas_menu.Menu_kantin_Base)
def create_menu(menu_kantin: schemas_menu.Menu_kantin_Create, db: Session = Depends(connection.get_db)):
    db_user = services_menu.create_menu(menu_kantin=menu_kantin,db=db)

@router.get('/menu_kantin', response_model=List[schemas_menu.Menu_kantin_Base])
async def get_semua_menu(db:Session=Depends(connection.get_db)):
	return await services_menu.get_all_menu(db=db)

@router.get('/{id_kantin}', response_model=List[schemas_menu.Menu_kantin_Base])
async def get_menu_kantin(id_kantin: int, db:Session=Depends(connection.get_db)):
	return await services_menu.get_menu_kantin(id_kantin=id_kantin, db=db)

@router.put('/update', status_code=200)
async def update_ketersediaan_menu(id_kantin: int, id_menu: int, ketersediaan: str, db: Session=Depends(connection.get_db)):
	return await services_menu.update_ketersediaan(id_kantin=id_kantin, id_menu=id_menu, ketersediaan=ketersediaan, db=db)

@router.get('/pendapatan_kantin/{id_kantin}')
async def get_perkiraan_pendapatan(id_kantin: int, keramaian: int, db: Session=Depends(connection.get_db)):
	return await services_menu.get_pendapatan(id_kantin=id_kantin, keramaian=keramaian, db=db)