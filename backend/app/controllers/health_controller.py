from sqlalchemy.orm import Session

from app.services import health_service


def get_health(db: Session) -> dict:
    up = health_service.database_is_up(db)
    return {
        "status": "ok" if up else "degraded",
        "database": "ok" if up else "unreachable",
        "version": "0.1.0",
    }
