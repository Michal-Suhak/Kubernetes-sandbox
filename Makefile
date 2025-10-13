up:
	docker-compose up -d
	@echo "Services started!"
	@echo "FastAPI: http://localhost:8000/health"
	@echo "pgAdmin: http://localhost:5050"

down:
	docker-compose down

logs:
	docker-compose logs -f

restart:
	docker-compose restart

build:
	docker-compose build --no-cache

clean:
	docker-compose down -v --rmi all

migrate:
	@read -p "Enter migration message: " msg; \
	docker-compose exec fastapi uv run alembic revision --autogenerate -m "$$msg"

upgrade:
	docker-compose exec fastapi uv run alembic upgrade head

downgrade:
	docker-compose exec fastapi uv run alembic downgrade -1

shell:
	docker-compose exec fastapi /bin/sh

db-shell:
	docker-compose exec postgres psql -U fastapi_user -d fastapi_db

test:
	docker-compose exec fastapi pytest