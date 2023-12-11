import sqlite3
from aiogram.types import User
import settings
from sqlite3 import IntegrityError
import datetime
from utils.utils import add_months


class DB:
    def __init__(self, db_name: str):
        self._conn = sqlite3.connect(db_name)
        self._cursor = self._conn.cursor()

        users_table_query = """CREATE TABLE IF NOT EXISTS users(
                            user_id INTEGER PRIMARY KEY,
                            is_admin BOOLEAN,
                            name TEXT,
                            username TEXT,
                            language TEXT DEFAULT "ru",
                            UNIQUE(user_id)
                            )"""

        files_table_query = """
                        CREATE TABLE IF NOT EXISTS files (
                            file_id TEXT NOT NULL,
                            file_ext TEXT,
                            category TEXT,
                            file_name TEXT,
                            PRIMARY KEY (file_id),
                            UNIQUE(file_name)
                        )"""

        answers_table_query = """
                        CREATE TABLE IF NOT EXISTS answers(
                            answers_file TEXT NOT NULL,
                            answers_file_name TEXT,
                            test_file TEXT NOT NULL,
                            test_file_name TEXT,
                            FOREIGN KEY (test_file) REFERENCES files (file_id)
                        )"""

        subscribers_table_query = """
                                CREATE TABLE IF NOT EXISTS subscribers(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    user_id INT NOT NULL UNIQUE,
                                    start_period DATE,
                                    end_period DATE,
                                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                                )"""

        self._cursor.execute(files_table_query)
        self._cursor.execute(users_table_query)
        self._cursor.execute(answers_table_query)
        self._cursor.execute(subscribers_table_query)
        self._conn.commit()

    def get_all_users(self) -> list:
        self._cursor.execute("SELECT user_id FROM users")
        return [item[0] for item in self._cursor.fetchall()]

    def insert_file(
        self,
        file_id: str,
        file_ext: str = None,
        category: str = None,
        file_name: str = None,
    ) -> bool:
        try:
            query = "INSERT INTO files VALUES (?, ?, ?, ?)"
            self._cursor.execute(query, (file_id, file_ext, category, file_name))
            self._conn.commit()
            return True
        except IntegrityError:
            return False

    def select_by(self, category: str) -> list:
        query = "SELECT * FROM files WHERE category = ?"
        self._cursor.execute(query, (category,))
        result = self._cursor.fetchall()
        return result

    def add_user(self, user: User):
        if user.id not in self.get_all_users():
            query = "INSERT INTO users (user_id, is_admin, name, username) VALUES (?, ?, ?, ?)"
            parameter_set = (
                user.id,
                user.id in settings.admins,
                user.full_name,
                user.username,
            )

            self._cursor.execute(query, parameter_set)

            self._conn.commit()

    def add_answers(
        self,
        test_file_id: str,
        answer_file_id: str,
        answer_file_name: str,
        test_file_name: str,
    ) -> None:
        query = "INSERT INTO answers VALUES (?, ?, ?, ?)"
        self._cursor.execute(
            query, (answer_file_id, answer_file_name, test_file_id, test_file_name)
        )
        self._conn.commit()

    def get_answers(self, test_file_id: str) -> str:
        query = "SELECT answers_file FROM answers WHERE test_file = ?"
        self._cursor.execute(query, (test_file_id,))
        return self._cursor.fetchone()[0]

    def replace_answer_file(
        self, test_file_name: str, answer_file_id: str, answer_file_name: str
    ) -> None:
        query = "UPDATE answers SET answers_file = ?, answers_file_name = ? WHERE test_file_name = ?"
        self._cursor.execute(query, (answer_file_id, answer_file_name, test_file_name))
        self._conn.commit()

    def file_exists(self, test_file_name: str) -> bool:
        query = "SELECT test_file_name FROM answers WHERE test_file_name = ?"
        self._cursor.execute(query, (test_file_name,))
        try:
            return bool(self._cursor.fetchone()[0])
        except TypeError:
            return False

    def user_exists(self, user: User) -> bool:
        query = "SELECT * FROM users WHERE user_id = ?"
        self._cursor.execute(query, (user.id,))
        return self._cursor.fetchone()

    def user_is_subscribed(self, user: User) -> bool:
        query = "SELECT * FROM subscribers WHERE user_id = ?"
        self._cursor.execute(query, (user.id,))
        return self._cursor.fetchone()

    def subscribe_user(self, user: User) -> None:
        query = """INSERT INTO subscribers (user_id, start_period, end_period) VALUES (?, ?, ?)"""

        start_period = datetime.datetime.now().date()
        end_period = add_months(start_period, 1).date()

        self._cursor.execute(query, (user.id, start_period, end_period))
        self._conn.commit()

    def unsubscribe_user(self, user_id: int) -> None:
        query = "DELETE FROM subscribers WHERE user_id = ?"
        self._cursor.execute(query, (user_id,))
        self._conn.commit()

    def change_language(self, user: User, lang: str):
        query = "UPDATE users SET language = ? WHERE user_id = ?"
        self._cursor.execute(query, (lang, user.id))
        self._conn.commit()

    def get_all_subscription_ends(self):
        query = "SELECT user_id, end_period FROM subscribers"
        self._cursor.execute(query)
        return self._cursor.fetchall()


db = DB(settings.db_name)
