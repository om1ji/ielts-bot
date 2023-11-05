import sqlite3
from aiogram.types import User
import settings


class DB:
    def __init__(self, db_name: str):
        self._conn = sqlite3.connect(db_name)
        self._cursor = self._conn.cursor()

        users_table_query = """CREATE TABLE IF NOT EXISTS users(
                            user_id INTEGER,
                            is_admin BOOLEAN,
                            name TEXT,
                            username TEXT,
                            UNIQUE(user_id)
                            )"""

        files_table_query = """
                        CREATE TABLE IF NOT EXISTS files (
                            id INTEGER PRIMARY KEY,
                            file_id TEXT NOT NULL,
                            file_ext TEXT,
                            category TEXT
                        )"""
        self._cursor.execute(files_table_query)
        self._cursor.execute(users_table_query)
        self._conn.commit()

    def get_all_users(self) -> list:
        self._cursor.execute("SELECT user_id FROM users")
        return [item[0] for item in self._cursor.fetchall()]

    def insert_file(
        self, file_id: str, file_ext: str = None, category: str = None
    ) -> None:
        query = "INSERT INTO files (file_id, file_ext, category) VALUES (?, ?, ?)"
        self._cursor.execute(query, (file_id, file_ext, category))
        self._conn.commit()

    def select_by(self, category: str) -> list:
        query = "SELECT * FROM files WHERE category = ?"
        self._cursor.execute(query, (category,))
        result = self._cursor.fetchall()
        return result

    def is_admin(self, user: User) -> bool:
        query = "SELECT is_admin FROM users WHERE user_id = ?"
        self._cursor.execute(query, (user.id,))
        return self._cursor.fetchall()[0][0]

    def add_user(self, user: User):
        if user.id not in self.get_all_users():
            query = "INSERT INTO users VALUES (?, ?, ?, ?)"
            parameter_set = (
                user.id,
                user.id in settings.admins,
                user.full_name,
                user.username,
            )

            self._cursor.execute(query, parameter_set)

            self._conn.commit()


db = DB(settings.db_name)
