
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env", override=True)


def get_db_connection():
    """Connect Flask routes to Supabase PostgreSQL."""
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL missing from .env")

    return psycopg.connect(
        database_url,
        connect_timeout=15,
        row_factory=dict_row,
    )


def init_db():
    """Check the PostgreSQL connection; tables were migrated already."""
    with get_db_connection() as connection:
        connection.execute("SELECT 1")

    print("Supabase PostgreSQL connection verified.")


if __name__ == "__main__":
    init_db()
    print("Database connection initialized successfully.")
