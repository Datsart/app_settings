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
                        feature TEXT NOT NULL,
                        attribute TEXT NOT NULL,
                        value INTEGER NOT NULL,
                        create_time timestamp DEFAULT CURRENT_TIMESTAMP,
                        update_time timestamp DEFAULT CURRENT_TIMESTAMP) '''
    dbConnection.execute(text(sql))
    dbConnection.commit()
    # # проверка на заполненность таблицы
    # select_query = "SELECT * FROM settings LIMIT 1"
    # result = dbConnection.execute(text(select_query)).fetchone()
    #
    # if result:
    #     print("Таблица уже заполнена")
    # else:
    #     from sqlalchemy.orm import declarative_base
    #     Base = declarative_base()
    #
    #     class DB(Base):
    #         __tablename__ = 'settings'
    #         id = Column(Integer, primary_key=True, nullable=False)
    #         feature = Column(String, nullable=False)
    #         attribute = Column(String, nullable=False)
    #         value = Column(String, nullable=False)
    #         create_time = Column(DateTime, default=datetime.now)
    #         update_time = Column(DateTime, default=datetime.now)
    #
    #     engine = create_engine('sqlite:////Users/artemdatsenko/PycharmProjects/app_settings/database.db')
    #     Base.metadata.create_all(engine)
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #     info = DB(
    #         feature='Some Feature',
    #         attribute='Some Attribute',
    #         value='Some Value',
    #         create_time=datetime.now(),
    #         update_time=datetime.now(),
    #     )
    #     session.add(info)
    #     session.commit()
    dbConnection.close()

# create_db_func()
