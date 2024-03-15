import webview
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from create_db import create_db_func

# from structure import settings_dict

current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, 'templates')
static_folder = os.path.join(current_dir, 'static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

absolute_path_db = '/Users/artemdatsenko/PycharmProjects/app_settings/database.db'  # ваш путь к БД
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{absolute_path_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DB(db.Model):
    '''модель БД'''
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    feature = db.Column(db.String, nullable=False)
    attribute = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)


def settings_dict():
    settings_dictionary = {
        'interface': {
            'demo_gui_on_full_screen_without_borders': {
                'text': 'Отображать на весь экран без границы:',
                'value': get_value_by_text('Отображать на весь экран без границы:') if get_value_by_text(
                    'Отображать на весь экран без границы:') else 0,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'checkbox',
            },
            'demo_monitor_index': {
                'text': 'Индекс монитора:',
                'value': get_value_by_text('Индекс монитора:') if get_value_by_text('Индекс монитора:') else 0,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
            'face_rectangle_border_size': {
                'text': 'Толщина обводки найденного лица:',
                'value': get_value_by_text('Толщина обводки найденного лица:') if get_value_by_text(
                    'Толщина обводки найденного лица:') else 3,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            }
        },
        'camera': {
            'video_path': {
                'text': 'Rtsp адрес или индекс вебкамеры:',
                'value': get_value_by_text('Rtsp адрес или индекс вебкамеры:') if get_value_by_text(
                    'Rtsp адрес или индекс вебкамеры:') else 0,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'text',
            },
            'video_read_width': {
                'text': 'Разрешение входного видео (ширина):',
                'value': get_value_by_text('Разрешение входного видео (ширина):') if get_value_by_text(
                    'Разрешение входного видео (ширина):') else 1920,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
            'video_read_height': {
                'text': 'Разрешение входного видео (высота):',
                'value': get_value_by_text('Разрешение входного видео (высота):') if get_value_by_text(
                    'Разрешение входного видео (высота):') else 1080,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
            'fps': {
                'text': 'FPS:',
                'value': get_value_by_text('FPS') if get_value_by_text('FPS') else 10,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
            'det_size_x': {
                'text': 'Сжатие для insightface (ширина):',
                'value': get_value_by_text('Сжатие для insightface (ширина):') if get_value_by_text(
                    'Сжатие для insightface (ширина):') else 256,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
            'det_size_y': {
                'text': 'Сжатие для insightface (высота):',
                'value': get_value_by_text('Сжатие для insightface (высота):') if get_value_by_text(
                    'Сжатие для insightface (высота):') else 256,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
            'scale_percent': {
                'text': 'Процент сжатия входного кадра (1/2) (1/3) и т.п:',
                'value': get_value_by_text('Процент сжатия входного кадра (1/2) (1/3) и т.п:') if get_value_by_text(
                    'Процент сжатия входного кадра (1/2) (1/3) и т.п:') else 1,
                'default': 'True if empty() else будет значение из БД',
                'data_type': 'number',
            },
        },
    }
    return settings_dictionary


def get_value_by_text(text):
    '''функция для поиска значений в БД по названию параметра'''
    with app.app_context():
        setting = DB.query.filter_by(attribute=text).first()
        if setting:
            return setting.value


@app.route('/', methods=['GET', 'POST'])
def redirect_to_route():
    return redirect('/app')


@app.route('/send_structute', methods=['GET', 'POST'])
def send_structute():
    '''роут на отправку данных'''
    counter = 0
    # проверка на пустая БД или нет
    if len(DB.query.all()) == 0:  # если пустая то заполняем значениями по умолчанию
        for category, parameters in settings_dict().items():
            for parameter, info in parameters.items():
                text = info['text']
                value = info['value']
                info = DB(
                    feature=category,
                    attribute=text,
                    value=value,
                    create_time=datetime.now(),
                    update_time=datetime.now(),
                )
                db.session.add(info)
                db.session.commit()
    return settings_dict()


@app.route('/post_response', methods=['GET', 'POST'])
def take_info():
    '''роут на принятие данных'''
    data = request.get_json()  # ответ с фронта

    def old_data():
        '''тут старые данные из БД'''
        old_list = []
        for k in DB.query.all():
            old_list.append(int(k.value))
        return old_list

    res_old_data = old_data()

    if len(DB.query.all()) != 0:  # если НЕ пустая БД,  то обновляем данные
        new_list_values = []
        list_params = []
        for i in settings_dict():
            for j in settings_dict()[i]:
                list_params.append(j)

        counter_id = 1
        counter_list = 0

        while counter_list < len(list_params):
            obj = db.session.get(DB, counter_id)
            obj.value = data[list_params[counter_list]]
            new_list_values.append(int(obj.value))
            counter_id += 1
            counter_list += 1
            db.session.commit()
    # код для обновления времени измененного элемента

    different_indices = [i for i, (new, old) in enumerate(zip(new_list_values, res_old_data)) if new != old]
    for i in different_indices:
        print(i)
        object_DB = DB.query.get(i + 1)
        if object_DB:
            object_DB.update_time = datetime.now()
            db.session.commit()

    return data


@app.route('/app', methods=['GET', 'POST'])
def login():
    full_url = request.url_root + 'send_structute'
    url_for_post = request.url_root + 'post_response'
    return render_template('index_1.html', full_url=full_url, url_for_post=url_for_post)


if __name__ == '__main__':
    '''закоментить нужное для развертывания в окне или в браузере'''
    create_db_func()
    app.run(host='127.0.0.1', port=5050, debug=True)
    # webview.create_window('App', app)
    # webview.start()
