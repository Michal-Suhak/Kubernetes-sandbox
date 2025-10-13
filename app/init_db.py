"""
Database initialization script

Run this once to create all tables in the database.
"""
from app.database import engine
from app.models import Base

def init_db():
    """
    Create all database tables based on SQLAlchemy models
    """
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    init_db()