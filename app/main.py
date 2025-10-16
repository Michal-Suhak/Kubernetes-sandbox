from fastapi import FastAPI

from app.routers import health, users

# Create FastAPI app
app = FastAPI(
    title="FastAPI User Management",
    description="User management API with PostgreSQL backend running on Kubernetes",
    version="1.0.0"
)

# Include routers
app.include_router(health.router)
app.include_router(users.router)
