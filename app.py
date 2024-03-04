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
                # 'value': db.session.get(DB, 10).value if db.session.get(DB, 10) else 0,
                'value': 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'demo_monitor_index': {
                'text': 'Индекс монитора:',
                # 'value': db.session.get(DB, 8).value if db.session.get(DB, 8) else 0,
                'value': 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'face_rectangle_border_size': {
                'text': 'Толщина обводки найденного лица:',
                # 'value': db.session.get(DB, 9).value if db.session.get(DB, 9) else 3,
                'value': 3,
                'default': 'True if empty() else будет значение из БД',
            }
        },
        'camera': {
            'video_path': {
                'text': 'Rtsp адрес или индекс вебкамеры:',
                # 'value': db.session.get(DB, 1).value if db.session.get(DB, 1) else 0,
                'value': 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'video_read_width': {
                'text': 'Разрешение входного видео (ширина):',
                # 'value': db.session.get(DB, 2).value if db.session.get(DB, 2) else 1920,
                'value': 1920,
                'default': 'True if empty() else будет значение из БД',
            },
            'video_read_height': {
                'text': 'разрешение входного видео (высота):',
                # 'value': db.session.get(DB, 3).value if db.session.get(DB, 3) else 1080,
                'value': 1080,
                'default': 'True if empty() else будет значение из БД',
            },
            'fps': {
                'text': 'FPS:',
                # 'value': db.session.get(DB, 4).value if db.session.get(DB, 4) else 10,
                'value': 10,
                'default': 'True if empty() else будет значение из БД',
            },
            'det_size_x': {
                'text': 'Сжатие для insightface (ширина):',
                # 'value': db.session.get(DB, 5).value if db.session.get(DB, 5) else 256,
                'value': 256,
                'default': 'True if empty() else будет значение из БД',
            },
            'det_size_y': {
                'text': 'Сжатие для insightface (высота):',
                # 'value': db.session.get(DB, 6).value if db.session.get(DB, 6) else 256,
                'value': 256,
                'default': 'True if empty() else будет значение из БД',
            },
            'scale_percent': {
                'text': 'Процент сжатия входного кадра (1/2) (1/3) и т.п:',
                # 'value': db.session.get(DB, 7).value if db.session.get(DB, 7) else '(1 / 1)',
                'value': 1,
                'default': 'True if empty() else будет значение из БД',
            },
        },
    }
    return settings_dictionary


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

    # print(data)

    def old_data():
        '''тут старые данные из БД'''
        old_list = []
        for k in DB.query.all():
            old_list.append(int(k.value))
        return old_list

    res_old_data = old_data()
    # counter = 0
    #
    # for i, j in data.items():
    #
    #     if counter <= 6:
    #         info = DB(
    #             feature=a[0],
    #             attribute=i,
    #             value=j,
    #             create_time=datetime.now(),
    #             update_time=datetime.now(),
    #         )
    #         db.session.add(info)
    #         db.session.commit()
    #         counter += 1
    #     else:
    #         info = DB(
    #             feature=a[1],
    #             attribute=i,
    #             value=j,
    #             create_time=datetime.now(),
    #             update_time=datetime.now(),
    #         )
    #         db.session.add(info)
    #         db.session.commit()
    # print(DB.query.filter(DB.attribute == 'Отображать на весь экран без границы:').first())

    if len(DB.query.all()) != 0:  # если НЕ пустая,  то обновляем данные
        new_list_values = []
        # for old_object in DB.query.all():
        #     attr = old_object.attribute
        #     new_obj = DB.query.filter(DB.attribute == f'{attr}').first()
        #     for i in settings_dict():
        #         for params in settings_dict()[i]:
        #
        #             new_obj.value = data[params]
        #             new_list_values.append(new_obj.value)
        # new_list = new_list_values[:len(DB.query.all())]
        # print(new_list)
        list_params = []
        for i in settings_dict():
            for j in settings_dict()[i]:
                list_params.append(j)

        counter_id = 1
        counter_list = 0

        while counter_list < len(list_params):
            obj = db.session.get(DB, counter_id)
            obj.value = data[list_params[counter_list]]
            new_list_values.append(obj.value)
            counter_id += 1
            counter_list += 1
            db.session.commit()
        # value_1 = db.session.get(DB, 1)
        # value_2 = db.session.get(DB, 2)
        # value_3 = db.session.get(DB, 3)
        # value_4 = db.session.get(DB, 4)
        # value_5 = db.session.get(DB, 5)
        # value_6 = db.session.get(DB, 6)
        # value_7 = db.session.get(DB, 7)
        # value_8 = db.session.get(DB, 8)
        # value_9 = db.session.get(DB, 9)
        # value_10 = db.session.get(DB, 10)
        #
        # value_1.value = data['video_path']
        # new_list.append(value_1.value)
        # value_2.value = data['video_read_width']
        # new_list.append(value_2.value)
        # value_3.value = data['video_read_height']
        # new_list.append(value_3.value)
        # value_4.value = data['fps']
        # new_list.append(value_4.value)
        # value_5.value = data['det_size_x']
        # new_list.append(value_5.value)
        # value_6.value = data['det_size_y']
        # new_list.append(value_6.value)
        # value_7.value = data['scale_percent']
        # new_list.append(value_7.value)
        # value_8.value = data['demo_monitor_index']
        # new_list.append(value_8.value)
        # value_9.value = data['face_rectangle_border_size']
        # new_list.append(value_9.value)
        # value_10.value = data['demo_gui_on_full_screen_without_borders']
        # new_list.append(value_10.value)
        print(new_list_values)
        print(list_params)
        # db.session.commit()
    # код для обновления времени измененного элемента
    counter_a = 1
    target_id_list = []
    for i in res_old_data:
        for j in range(len(new_list_values)):
            if (int(i)) != new_list_values[counter_a - 1]:
                target_id_list.append(counter_a)
            break
        counter_a += 1
    for i in target_id_list:
        object_DB = db.session.get(DB, i)
        object_DB.update_time = datetime.now()
        db.session.commit()

    return data


@app.route('/app', methods=['GET', 'POST'])
def login():
    full_url = request.url_root + 'send_structute'
    url_for_post = request.url_root + 'post_response'
    return render_template('index.html', full_url=full_url, url_for_post=url_for_post)


if __name__ == '__main__':
    create_db_func()
    app.run(host='127.0.0.1', port=5050, debug=True)
    # webview.create_window('App', app)
    # webview.start()
