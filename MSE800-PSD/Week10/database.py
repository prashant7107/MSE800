import sqlite3


class DatabaseManager:
    # Handle SQLite database.

    def __init__(self, db_name="system.db"):
        self.db_name = db_name
        self._create_table()

    def _get_connection(self):
        # Create and return a database connection.
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        # Initialize the database schema if it doesn't exist.
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            security_question TEXT NOT NULL,
            security_answer_hash TEXT NOT NULL
        );
        """
        self.execute_query(query)

    def execute_query(self, query, params=()):
        # Execute write operations (INSERT, UPDATE, DELETE).
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

    def fetch_one(self, query, params=()):
        # Fetch a single record from the database.
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()