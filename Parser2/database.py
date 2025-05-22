import psycopg2
from psycopg2 import sql
from typing import List, Dict, Any

class Database:
    def __init__(self, dbname: str, user: str, password: str, host: str = "localhost", port: int = 5432):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        """Создаёт таблицу для вакансий, если её нет."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vacancies (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                salary INTEGER DEFAULT 0,
                employer TEXT NOT NULL,
                region_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        self.conn.commit()

    def save_vacancies(self, vacancies: List[Dict[str, Any]], region_id: int) -> bool:
        """Сохраняет список вакансий в БД."""
        try:
            for vacancy in vacancies:
                self.cursor.execute(
                    """
                    INSERT INTO vacancies (name, salary, employer, region_id)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (vacancy['name'], vacancy['salary'], vacancy['employer'], region_id)
                )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении в БД: {e}")
            self.conn.rollback()
            return False

    def close(self):
        self.cursor.close()
        self.conn.close()