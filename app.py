from settings import Settings
from create_db import create_db_func
import webview
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from structure import settings_dict

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


@app.route('/', methods=['GET', 'POST'])
def redirect_to_route():
    return redirect('/app')


@app.route('/send_structute', methods=['GET', 'POST'])
def send_structute():
    return settings_dict()


@app.route('/post_response', methods=['GET', 'POST'])
def take_info():
    data = request.get_json()
    print(data)

    return data


@app.route('/app', methods=['GET', 'POST'])
def login():
    # settings_data = DB.query.all()  # вытаскиваем зн-я из БД
    #
    # for i in settings_data:
    #     feature_value = i.feature if i.feature else ''
    #     attribute_value = i.attribute if i.attribute else ''
    #     value_value = i.value if i.value else ''
    #     create_time_value = i.create_time.strftime('%Y-%m-%d %H:%M:%S') if i.create_time else ''
    #     update_time_value = i.update_time.strftime('%Y-%m-%d %H:%M:%S') if i.update_time else ''
    # data = [{'feature': feature_value,
    #          'attribute_value': attribute_value,
    #          'video_read_height': value_value,
    #          'create_time': create_time_value,
    #          'update_time': update_time_value,
    #          }]
    full_url = request.url_root + 'send_structute'
    url_for_post = request.url_root + 'post_response'
    # print("Full URL for '/app':", full_url)
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
    app.run(host='127.0.0.1', port=5050, debug=True)
    # webview.create_window('App', app)
    # webview.start()
