from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.controllers import health_controller
from app.db.session import get_db

router = APIRouter(prefix="/api/v1", tags=["system"])


@router.get("/health")
def health(response: Response, db: Session = Depends(get_db)):
    payload = health_controller.get_health(db)
    if payload["database"] != "ok":
        response.status_code = 503
    return payload
