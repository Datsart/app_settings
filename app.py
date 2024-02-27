from settings import Settings
from create_db import create_db_func
import webview
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

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
                'value': db.session.get(DB, 10).value if db.session.get(DB, 10) else 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'demo_monitor_index': {
                'text': 'Индекс монитора:',
                'value': db.session.get(DB, 8).value if db.session.get(DB, 8) else 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'face_rectangle_border_size': {
                'text': 'Толщина обводки найденного лица:',
                'value': db.session.get(DB, 9).value if db.session.get(DB, 9) else 3,
                'default': 'True if empty() else будет значение из БД',
            }
        },
        'camera': {
            'video_path': {
                'text': 'Rtsp адрес или индекс вебкамеры:',
                'value': db.session.get(DB, 1).value if db.session.get(DB, 1) else 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'video_read_width': {
                'text': 'Разрешение входного видео (ширина):',
                'value': db.session.get(DB, 2).value if db.session.get(DB, 2) else 1920,
                'default': 'True if empty() else будет значение из БД',
            },
            'video_read_height': {
                'text': 'разрешение входного видео (высота):',
                'value': db.session.get(DB, 3).value if db.session.get(DB, 3) else 1080,
                'default': 'True if empty() else будет значение из БД',
            },
            'fps': {
                'text': 'FPS:',
                'value': db.session.get(DB, 4).value if db.session.get(DB, 4) else 10,
                'default': 'True if empty() else будет значение из БД',
            },
            'det_size_x': {
                'text': 'Сжатие для insightface (ширина):',
                'value': db.session.get(DB, 5).value if db.session.get(DB, 5) else 256,
                'default': 'True if empty() else будет значение из БД',
            },
            'det_size_y': {
                'text': 'Сжатие для insightface (высота):',
                'value': db.session.get(DB, 6).value if db.session.get(DB, 6) else 256,
                'default': 'True if empty() else будет значение из БД',
            },
            'scale_percent': {
                'text': 'Процент сжатия входного кадра (1/2) (1/3) и т.п:',
                'value': db.session.get(DB, 7).value if db.session.get(DB, 7) else '(1 / 1)',
                'default': 'True if empty() else будет значение из БД',
            },
        },
    }
    return settings_dictionary


@app.route('/', methods=['GET', 'POST'])
def redirect_to_route():
    return redirect('/app')


@app.route('/send_structute', methods=['GET', 'POST'])
# роут на отправку
def send_structute():
    return settings_dict()


@app.route('/post_response', methods=['GET', 'POST'])
# роут на принятие
def take_info():
    data = request.get_json()
    # print(data)

    counter = 0
    a = ['camera', 'interface']
    if len(DB.query.all()) == 0:
        for i, j in data.items():

            if counter <= 6:
                info = DB(
                    feature=a[0],
                    attribute=i,
                    value=j,
                    create_time=datetime.now(),
                    update_time=datetime.now(),
                )
                db.session.add(info)
                db.session.commit()
                counter += 1
            else:
                info = DB(
                    feature=a[1],
                    attribute=i,
                    value=j,
                    create_time=datetime.now(),
                    update_time=datetime.now(),
                )
                db.session.add(info)
                db.session.commit()
    else:
        value_1 = db.session.get(DB, 1)
        value_2 = db.session.get(DB, 2)
        value_3 = db.session.get(DB, 3)
        value_4 = db.session.get(DB, 4)
        value_5 = db.session.get(DB, 5)
        value_6 = db.session.get(DB, 6)
        value_7 = db.session.get(DB, 7)
        value_8 = db.session.get(DB, 8)
        value_9 = db.session.get(DB, 9)
        value_10 = db.session.get(DB, 10)
        value_1.value = data['video_path']
        value_2.value = data['video_read_width']
        value_3.value = data['video_read_height']
        value_4.value = data['fps']
        value_5.value = data['det_size_x']
        value_6.value = data['det_size_y']
        value_7.value = data['scale_percent']
        value_8.value = data['demo_monitor_index']
        value_9.value = data['face_rectangle_border_size']
        value_10.value = data['demo_gui_on_full_screen_without_borders']
        db.session.commit()
    return data


@app.route('/app', methods=['GET', 'POST'])
def login():
    # settings_data = DB.query.all()  # вытаскиваем зн-я из БД
    #
    # for i in settings_data:
    # feature_value = i.feature if i.feature else ''
    # attribute_value = i.attribute if i.attribute else ''
    # value_value = i.value if i.value else ''
    # create_time_value = i.create_time.strftime('%Y-%m-%d %H:%M:%S') if i.create_time else ''
    # update_time_value = i.update_time.strftime('%Y-%m-%d %H:%M:%S') if i.update_time else ''
    full_url = request.url_root + 'send_structute'
    url_for_post = request.url_root + 'post_response'
    return render_template('index.html', full_url=full_url, url_for_post=url_for_post)


# def send_settings():
#     settings_data = {
#         'feature': 'значение_фичи',
#         'attribute': 'значение_атрибута',
#         'value': 'значение_значения',
#         'create_time': 'время_создания',
#         'update_time': 'время_обновления'
#     }
#     return jsonify(settings_data)

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5050, debug=True)
    webview.create_window('App', app)
    webview.start()
