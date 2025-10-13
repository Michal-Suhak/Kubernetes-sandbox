FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Enable BuildKit to use parent context
# Build with: docker build -t fastapi-app -f app/Dockerfile .
# Or from app dir: docker build -t fastapi-app -f Dockerfile ..

# Copy dependency files from parent
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Copy application code
COPY app/ ./app/

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
