import sqlite3
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


def create_db_func(feature, attribute, value, create_time, update_time):
    try:
        with sqlite3.connect(database='database.db') as connection:
            cursor = connection.cursor()
            print('Создана новая БД')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    ID INTEGER PRIMARY KEY,
                    feature TEXT NOT NULL,
                    attribute TEXT NOT NULL,
                    value TEXT NOT NULL,
                    create_time timestamp,
                    update_time timestamp
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
            ''', (feature, attribute, value, create_time, update_time))

            connection.commit()
            print('Создана новая таблица')

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# create_db_func('camera', 1920, 1080, current_time, current_time)
