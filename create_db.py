import sqlite3


def create_db_func(video_path, video_read_width, video_read_height, fps, det_size, scale_percent):
    try:
        with sqlite3.connect(database='database.db') as connection:
            cursor = connection.cursor()
            print('Создана новая БД')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    ID INTEGER PRIMARY KEY,
                    video_path TEXT NOT NULL,
                    video_read_width INTEGER NOT NULL,
                    video_read_height INTEGER NOT NULL,
                    fps INTEGER NOT NULL,
                    det_size_x INTEGER NOT NULL,
                    det_size_y INTEGER NOT NULL,
                    scale_percent INTEGER NOT NULL
                )
            ''')

            cursor.execute('''
                INSERT INTO settings (
                    video_path, 
                    video_read_width, 
                    video_read_height, 
                    fps, 
                    det_size_x, 
                    det_size_y, 
                    scale_percent
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (video_path, video_read_width, video_read_height, fps, *det_size, scale_percent))

            connection.commit()
            print('Создана новая таблица')

    except Exception as e:
        print(f"Произошла ошибка: {e}")


create_db_func('', 1920, 1080, 30, ('', 123321), 80)
