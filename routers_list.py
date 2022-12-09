from typing import List
from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
import services_list, schemas_list, models_list

app = FastAPI()
router = APIRouter(
	prefix='/list_kantin',
	tags=['List_kantin']
)

models_list.connection.Base.metadata.create_all(bind=connection.engine)

@router.post("/list_kantin", response_model=schemas_list.List_kantin_Base)
def create_list(list_kantin: schemas_list.List_kantin_Create, db: Session = Depends(connection.get_db)):
    db_user = services_list.create_list(list_kantin=list_kantin,db=db)

@router.get('/list_kantin', response_model=List[schemas_list.List_kantin_Base])
async def get_semua_list(db:Session=Depends(connection.get_db)):
	return await services_list.get_all_list(db=db)