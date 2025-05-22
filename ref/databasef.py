import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection():
    conn = sqlite3.connect('plants.db')
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with db_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("DROP TABLE IF EXISTS plants")
        cursor.execute("DROP TABLE IF EXISTS care_guide")
        
        cursor.execute('''
            CREATE TABLE plants (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                difficulty TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE care_guide (
                plant_id INTEGER PRIMARY KEY,
                watering TEXT NOT NULL,
                light TEXT NOT NULL,
                FOREIGN KEY (plant_id) REFERENCES plants(id)
            )
        ''')
        
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_plant_name_search 
            ON plants(LOWER(TRIM(name)))
        ''')
        
        cursor.executemany(
            "INSERT INTO plants VALUES (?, ?, ?)",
            [
                (1, 'Фикус', 'средне'),
                (2, 'Кактус', 'легко')
            ]
        )
        
        cursor.executemany(
            "INSERT INTO care_guide VALUES (?, ?, ?)",
            [
                (1, 'Умеренный', 'Яркий свет'),
                (2, 'Редкий', 'Прямое солнце')
            ]
        )
        conn.commit()

def get_plant(plant_name):
    with db_connection() as conn:
        cursor = conn.cursor()
        
        explain_query = '''
            EXPLAIN QUERY PLAN
            SELECT p.name, p.difficulty, c.watering, c.light
            FROM plants p
            JOIN care_guide c ON p.id = c.plant_id
            WHERE LOWER(TRIM(p.name)) = LOWER(TRIM(?))
        '''
        cursor.execute(explain_query, (plant_name.strip(),))
        print("\nПлан выполнения запроса:")
        for row in cursor:
            print(f"• {row['detail']}")
    
        main_query = '''
            SELECT p.name, p.difficulty, c.watering, c.light
            FROM plants p
            JOIN care_guide c ON p.id = c.plant_id
            WHERE LOWER(TRIM(p.name)) = LOWER(TRIM(?))
        '''
        cursor.execute(main_query, (plant_name.strip(),))
        return cursor.fetchone()