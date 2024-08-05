import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    """Class to manage the database connection."""

    def __init__(self):
        """Initialize database connection parameters from environment variables."""
        self.dbname = os.getenv("DATABASE_NAME")
        self.user = os.getenv("DB_USERNAME")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = os.getenv("DB_PORT")
        self.connection = None

    def connect(self):
        """Establish a connection to the database."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except OperationalError as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
