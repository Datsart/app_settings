import sqlite3
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


def create_db_func():
    try:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            print('Создана новая БД')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    ID INTEGER PRIMARY KEY,
                    feature TEXT NOT NULL,
                    attribute TEXT NOT NULL,
                    value TEXT NOT NULL,
                    create_time timestamp DEFAULT CURRENT_TIMESTAMP,
                    update_time timestamp DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            cursor.execute('''
                INSERT INTO settings (
                    feature, 
                    attribute, 
                    value, 
                    create_time, 
                    update_time
                ) VALUES (?, ?, ?, ?, ?)
            ''', ())

            connection.commit()
            print('Создана новая таблица')

    except Exception as e:
        print(f"Произошла ошибка: {e}")


create_db_func()
