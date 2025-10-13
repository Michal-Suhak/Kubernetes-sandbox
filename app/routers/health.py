"""
Health check and monitoring endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.config import DATABASE_NAME

router = APIRouter(tags=["health"])


@router.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World", "app": "FastAPI User Management"}


@router.get("/health")
async def health_check():
    """
    Simple health check endpoint

    Returns basic health status without database check
    """
    return {"status": "healthy"}


@router.get("/db-health")
def db_health_check(db: Session = Depends(get_db)):
    """
    Database health check

    Verifies connection to PostgreSQL database
    """
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "database connected",
            "database": DATABASE_NAME
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {str(e)}"
        )


@router.get("/oom-test")
async def oom_test():
    """
    OOM (Out Of Memory) test endpoint

    WARNING: This will crash the pod for Kubernetes testing!
    Allocates memory until OOMKilled
    """
    memory_hog = []
    try:
        # Allocate memory in 100MB chunks until OOMKilled
        while True:
            memory_hog.append(" " * (100 * 1024 * 1024))
    except MemoryError:
        return {"status": "MemoryError caught (shouldn't reach here)"}
    return {"status": "completed"}