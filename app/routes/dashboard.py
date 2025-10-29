from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.schemas.dashboard import DashboardCounts
from app.crud import dashboard as crud_dashboard

app = APIRouter()

@app.get("/counts", response_model=DashboardCounts)
def get_counts(db: Session = Depends(get_db)):
    return crud_dashboard.get_dashboard_counts(db)


@app.get("/sales")
def sales_dashboard(db: Session = Depends(get_db)):
    return crud_dashboard.get_sales_by_month(db)
