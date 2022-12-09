from fastapi import FastAPI

import uvicorn

# Routers yang digunakan
import routers_list as list_router
import routers_menu as menu_router
from auth import routers as auth_router

app = FastAPI()

# Include semua routers
app.include_router(auth_router.router)
app.include_router(list_router.router)
app.include_router(menu_router.router)

@app.get("/")
async def home():
	return {"Selamat Datang di Layanan TST Kantin ITB": "Silahkan Login untuk Menggunakan Layanan"}

if __name__ == '__main__':
	uvicorn.run('main:app', host='0.0.0.0', port=8003, reload=True)