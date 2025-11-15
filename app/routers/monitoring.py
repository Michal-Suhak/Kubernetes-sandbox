from fastapi import APIRouter
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

router = APIRouter(tags=["monitoring"])

# Prometheus Metrics
REQUEST_COUNT = Counter(
    'fastapi_requests_total',
    'Total requests',
    ['method', 'endpoint', 'status']
)

REQUEST_DURATION = Histogram(
    'fastapi_request_duration_seconds',
    'Request duration in seconds',
    ['method', 'endpoint']
)

DB_QUERIES = Counter(
    'fastapi_db_queries_total',
    'Total database queries',
    ['query_type']
)

@router.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
