from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import get_db
from app.schemas.health import DatabaseHealthResponse, HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "",
    response_model=HealthResponse,
    summary="Service Health Check",
    description="Returns the general operational health status of the application.",
)
def health_check() -> HealthResponse:
    """Check general application health."""
    return HealthResponse(
        status="ok",
        service=settings.SERVICE_NAME,
    )


@router.get(
    "/db",
    response_model=DatabaseHealthResponse,
    responses={
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "model": DatabaseHealthResponse,
            "description": "PostgreSQL database is unreachable or query failed",
        }
    },
    summary="Database Health Check",
    description="Verifies direct connectivity with the PostgreSQL database by executing a probe query.",
)
def database_health_check(db: Session = Depends(get_db)):
    """Check PostgreSQL connectivity.

    Executes a lightweight query (SELECT 1). Returns HTTP 200 if connected,
    or HTTP 503 if unavailable. Never returns a fake success.
    """
    try:
        db.execute(text("SELECT 1"))
        return DatabaseHealthResponse(
            status="ok",
            database="connected",
            detail="PostgreSQL connection verified successfully",
        )
    except Exception as exc:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "error",
                "database": "disconnected",
                "detail": f"Database health check failed: {str(exc)}",
            },
        )
