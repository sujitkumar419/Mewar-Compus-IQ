
import sqlite3
import os
from pathlib import Path
from datetime import datetime

import psycopg
from dotenv import load_dotenv


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
SQLITE_PATH = BASE_DIR / "campus_iq.db"

load_dotenv(BASE_DIR / ".env", override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

TABLES = [
    "users",
    "user_uploaded_documents",
    "user_pdf_context",
    "activity",
]


def convert_timestamp(value):
    """Convert SQLite timestamp strings to Python datetime objects."""
    if value is None or isinstance(value, datetime):
        return value

    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            raise ValueError(f"Unrecognized timestamp format: {value!r}")

    return value


def main():
    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL missing. Check your .env file."
        )

    if not SQLITE_PATH.exists():
        raise FileNotFoundError(
            f"SQLite database not found: {SQLITE_PATH}"
        )

    sqlite_conn = None
    postgres_conn = None

    try:
        # Connect to the source SQLite database.
        sqlite_conn = sqlite3.connect(SQLITE_PATH)
        sqlite_conn.row_factory = sqlite3.Row
        sqlite_conn.execute("PRAGMA foreign_keys = ON")

        # Read source data in parent-first order.
        source_data = {}

        for table in TABLES:
            rows = sqlite_conn.execute(
                f"SELECT * FROM {table}"
            ).fetchall()

            source_data[table] = [
                dict(row) for row in rows
            ]

        print("LOCAL SQLITE RECORDS")
        for table in TABLES:
            print(f"{table}: {len(source_data[table])}")

        # Connect to Supabase PostgreSQL.
        postgres_conn = psycopg.connect(
            DATABASE_URL,
            connect_timeout=15,
        )

        # All PostgreSQL changes happen in one transaction.
        with postgres_conn.transaction():
            with postgres_conn.cursor() as cur:

                # Stop if any destination table already has data.
                # This prevents accidental duplicate migrations.
                print("\nChecking Supabase destination...")

                for table in TABLES:
                    cur.execute(
                        f"SELECT COUNT(*) FROM public.{table}"
                    )
                    count = cur.fetchone()[0]

                    if count != 0:
                        raise RuntimeError(
                            f"Supabase table '{table}' already "
                            f"contains {count} rows. "
                            "Migration stopped without inserting data."
                        )

                print("All destination tables are empty.")

                # Verify there are no broken user references.
                user_ids = {
                    row["id"] for row in source_data["users"]
                }

                for table in [
                    "user_uploaded_documents",
                    "user_pdf_context",
                    "activity",
                ]:
                    for row in source_data[table]:
                        if row["user_id"] not in user_ids:
                            raise ValueError(
                                f"Invalid user_id in {table}: "
                                f"{row['user_id']}"
                            )

                # Insert records while preserving original IDs.
                column_order = {
                    "users": [
                        "id", "name", "email",
                        "password_hash", "created_at"
                    ],
                    "user_uploaded_documents": [
                        "id", "user_id", "filename",
                        "extension", "extracted_text",
                        "uploaded_at"
                    ],
                    "user_pdf_context": [
                        "user_id", "filename",
                        "extracted_text", "uploaded_at"
                    ],
                    "activity": [
                        "id", "user_id", "activity_type",
                        "details", "created_at"
                    ],
                }

                for table in TABLES:
                    rows = source_data[table]

                    if not rows:
                        print(f"\n{table}: no records to copy")
                        continue

                    columns = column_order[table]

                    placeholders = ", ".join(
                        ["%s"] * len(columns)
                    )
                    column_sql = ", ".join(columns)

                    insert_sql = (
                        f"INSERT INTO public.{table} "
                        f"({column_sql}) "
                        f"VALUES ({placeholders})"
                    )

                    values = []

                    for row in rows:
                        record = []

                        for column in columns:
                            value = row[column]

                            if column in (
                                "created_at",
                                "uploaded_at",
                            ):
                                value = convert_timestamp(value)

                            record.append(value)

                        values.append(tuple(record))

                    cur.executemany(insert_sql, values)

                    print(
                        f"{table}: inserted {len(values)} records"
                    )

                # Reset PostgreSQL identity sequences so future
                # inserts do not reuse IDs already migrated.
                for table in [
                    "users",
                    "user_uploaded_documents",
                    "activity",
                ]:
                    cur.execute(
                        "SELECT pg_get_serial_sequence(%s, %s)",
                        (f"public.{table}", "id"),
                    )
                    sequence_name = cur.fetchone()[0]

                    if sequence_name:
                        cur.execute(
                            f"SELECT COALESCE(MAX(id), 0) "
                            f"FROM public.{table}"
                        )
                        max_id = cur.fetchone()[0]

                        if max_id == 0:
                            cur.execute(
                                "SELECT setval(%s::regclass, %s, %s)",
                                (sequence_name, 1, False),
                            )
                        else:
                            cur.execute(
                                "SELECT setval(%s::regclass, %s, %s)",
                                (sequence_name, max_id, True),
                            )

        # Transaction committed successfully.
        print("\nMIGRATION SUCCESSFUL")
        print("Verifying Supabase record counts...")

        with postgres_conn.cursor() as cur:
            for table in TABLES:
                cur.execute(
                    f"SELECT COUNT(*) FROM public.{table}"
                )
                destination_count = cur.fetchone()[0]
                source_count = len(source_data[table])

                status = (
                    "OK"
                    if source_count == destination_count
                    else "COUNT MISMATCH"
                )

                print(
                    f"{table}: SQLite={source_count}, "
                    f"Supabase={destination_count} [{status}]"
                )

                if source_count != destination_count:
                    raise RuntimeError(
                        f"Record count mismatch in {table}"
                    )

        print("\nAll record counts verified.")

    except Exception as error:
        print("\nMIGRATION FAILED")
        print(f"Error type: {type(error).__name__}")
        print(f"Details: {error}")
        print(
            "PostgreSQL transaction was rolled back if "
            "the error occurred during migration."
        )
        raise

    finally:
        if sqlite_conn is not None:
            sqlite_conn.close()

        if postgres_conn is not None:
            postgres_conn.close()


if __name__ == "__main__":
    main()
