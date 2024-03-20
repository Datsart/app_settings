import webview
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from create_db import create_db_func
from structure import settings_dict
import re

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
    parameter = db.Column(db.String, nullable=False)
    attribute = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)


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
                    parameter=parameter,
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
            old_list.append(k.value)
        return old_list

    res_old_data = old_data()

    if len(DB.query.all()) != 0:  # если НЕ пустая БД,  то обновляем данные

        # параметры структуры ДО добавления новых полей
        old_list_params = []
        for i in DB.query.all():
            old_list_params.append(i.parameter)
        # print(old_list_params, ' old list')
        # параметры структуры ПОЛСЕ добавления новых полей
        new_list_values = []
        new_list_params = []
        for i in settings_dict():
            for j in settings_dict()[i]:
                if j not in old_list_params:
                    print(j)
                    # список получается только из тех элементов которые добавили
                    new_list_params.append(j)

        # проверяем на добавление нового поля в БД
        for new_param in new_list_params:
            if new_param not in old_list_params:
                for category, parameters in settings_dict().items():
                    for parameter, info in parameters.items():
                        if parameter == new_param:
                            text = info['text']
                            value = info['value']
                            info = DB(
                                feature=category,
                                parameter=parameter,
                                attribute=text,
                                value=value,
                                create_time=datetime.now(),
                                update_time=datetime.now(),
                            )
                            db.session.add(info)
                            db.session.commit()

        def is_numeric_string(input_str):
            '''выводит ТРУ если в строке целое или дробное число, если встречаются НЕ числа то фолс'''
            if type(input_str) == int:
                return True
            else:
                pattern = r"^[0-9]+(\.[0-9]+)?$"
                return bool(re.match(pattern, input_str))

        counter_id = 1
        counter_list = 0
        # к старому полному списку добавили новые добавленные поля
        new_list_params = old_list_params + new_list_params
        # обновили значения в БД
        while counter_list < len(new_list_params):
            obj = db.session.get(DB, counter_id)
            obj.value = data[new_list_params[counter_list]]
            if is_numeric_string(obj.value) == True:
                new_list_values.append(int(obj.value))
            else:
                new_list_values.append(obj.value)
            counter_id += 1
            counter_list += 1
            db.session.commit()

        # код для обновления времени измененного элемента
        different_indices = [i for i, (new, old) in enumerate(zip(new_list_values, res_old_data)) if new != old]
        for i in different_indices:
            object_DB = db.session.get(DB, i + 1)
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
