import sqlite3

def init_db():
    conn = sqlite3.connect('plants.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plants (
            id INTEGER,
            name TEXT,
            latin_name TEXT,
            difficulty TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS care_guide (
            plant_name TEXT,
            watering TEXT,
            light TEXT
        )
    ''')
    
    cursor.execute("DELETE FROM plants")
    cursor.execute("DELETE FROM care_guide")
    
    cursor.executemany(
        "INSERT INTO plants VALUES (?, ?, ?, ?)",
        [
            (1, 'Фикус', 'Ficus', 'средне'),
            (2, 'Кактус', 'Cactaceae', 'легко')
        ]
    )
    
    cursor.executemany(
        "INSERT INTO care_guide VALUES (?, ?, ?)",
        [
            ('Фикус', 'Умеренный', 'Яркий свет'),
            ('Кактус', 'Редкий', 'Прямое солнце')
        ]
    )
    
    conn.commit()
    conn.close()

def get_plant(plant_name):
    conn = sqlite3.connect('plants.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.id, p.name, p.latin_name, p.difficulty, 
               c.watering, c.light
        FROM plants p
        JOIN care_guide c ON p.name = c.plant_name
        WHERE p.name LIKE '%' || ? || '%'
    ''', (plant_name,))
    
    result = cursor.fetchall()
    conn.close()
    return result