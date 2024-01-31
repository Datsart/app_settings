from settings import Settings

import webview
from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, 'templates')
static_folder = os.path.join(current_dir, 'static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

absolute_path_db = '/Users/artemdatsenko/PycharmProjects/app_settings/database.db'  # ваш путь к БД
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{absolute_path_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DB(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    video_path = db.Column(db.String, nullable=False)
    video_read_width = db.Column(db.Integer, nullable=False)
    video_read_height = db.Column(db.Integer, nullable=False)
    fps = db.Column(db.Integer, nullable=False)
    det_size_x = db.Column(db.String, nullable=False)
    det_size_y = db.Column(db.String, nullable=False)
    scale_percent = db.Column(db.String, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def login():
    settings_data = DB.query.all()

    for i in settings_data:
        video_path_value = i.video_path if i.video_path else Settings.video_path
        video_read_width_value = i.video_read_width if i.video_read_width else Settings.video_read_width
        video_read_height_value = i.video_read_height if i.video_read_height else Settings.video_read_height
        fps_value = i.fps if i.fps else Settings.fps
        det_size_x_value = i.det_size_x if i.det_size_x else Settings.det_size
        det_size_y_value = i.det_size_y if i.det_size_y else Settings.det_size
        scale_percent_value = i.scale_percent if i.scale_percent else Settings.scale_percent
    data = [{'video_path_value': video_path_value,
             'video_read_width_value': video_read_width_value,
             'video_read_height_value': video_read_height_value,
             'fps_value': fps_value,
             'det_size_x_value': det_size_x_value,
             'det_size_y_value': det_size_y_value,
             'scale_percent_value': scale_percent_value}]
    return render_template('index.html', data=data)


if __name__ == '__main__':
    webview.create_window('App', app)
    webview.start()
