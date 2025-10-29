from fastapi import FastAPI
import uvicorn
from app.core.config import SessionLocal, engine

from app.routes.auth_routes import app as auth_app
from app.routes.user_routes import app as user_app

from app.routes.dashboard import app as dashboard_app

from app.routes.client_routes import app as client_app
from app.routes.room_routes import app as room_app
from app.routes.reservation_routes import app as reservation_app

from app.routes.reports_routes import app as reports_app

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_app, tags=['Auth'], prefix='/auth')
app.include_router(user_app, tags=['Users'], prefix='/users')

app.include_router(dashboard_app, tags=['Dashboard'], prefix='/dashboard')

app.include_router(client_app, tags=['Clients'], prefix='/clients')
app.include_router(room_app, tags=['Rooms'], prefix='/rooms')
app.include_router(reservation_app, tags=['Reservations'], prefix='/reservations')

app.include_router(reports_app, tags=["Reports"], prefix="/reports")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
