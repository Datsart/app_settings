from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database, drop_database


def create_db_func():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    DB_URI = 'sqlite:////Users/artemdatsenko/PycharmProjects/app_settings/database.db'
    if not database_exists(DB_URI):
        create_database(DB_URI)
        print('Создана новая БД')
    else:
        print('БД уже есть')

    def create_connection():
        """Вспомогательная функция создния соединения с БД"""
        alchemyEngine = create_engine(DB_URI)
        dbConnection = alchemyEngine.connect()
        return dbConnection

    dbConnection = create_connection()
    sql = ''' CREATE TABLE IF NOT EXISTS settings (
                        ID INTEGER PRIMARY KEY,
                        parameter TEXT NOT NULL,
                        feature TEXT NOT NULL,
                        attribute TEXT NOT NULL,
                        value INTEGER NOT NULL,
                        create_time timestamp DEFAULT CURRENT_TIMESTAMP,
                        update_time timestamp DEFAULT CURRENT_TIMESTAMP) '''
    dbConnection.execute(text(sql))
    dbConnection.commit()
    dbConnection.close()
