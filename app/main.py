from fastapi import FastAPI
import time

from app.routers import health, users, monitoring

# Create FastAPI app
app = FastAPI(
    title="FastAPI User Management",
    description="User management API with PostgreSQL backend running on Kubernetes",
    version="1.0.0"
)

# Middleware for Prometheus metrics collection
@app.middleware("http")
async def metrics_middleware(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    # Track request count and duration
    monitoring.REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    monitoring.REQUEST_DURATION.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(duration)

    return response

# Include routers
app.include_router(health.router)
app.include_router(users.router)
app.include_router(monitoring.router)
