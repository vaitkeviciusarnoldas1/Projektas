from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database engine (replace the URL with your database configuration)
engine = create_engine('sqlite:///gym_management.db')

# Create a base class for all tables
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
