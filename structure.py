settings_dict = {
    'interface': {
        'demo_gui_on_full_screen_without_borders': {
            'text': 'Отображать на весь экран без границы',
            'value': [True, False],
            'default': 'True if empty() else будет значение из БД',
        },
        'demo_monitor_index': {
            'text': '..........',  # не знаю что тут имелось ввиду
            'value': 0,
            'default': 'True if empty() else будет значение из БД',
        },
        'face_rectangle_border_size': {
            'text': 'толщина обводки найденного лица',
            'value': 3,
            'default': 'True if empty() else будет значение из БД',
        }
    },
    'camera': {
        'video_path': {
            'text': 'rtsp адрес или индекс вебкамеры',
            'value': 0,
            'default': 'True if empty() else будет значение из БД',
        },
        'video_read_width': {
            'text': 'разрешение входного видео (ширина)',
            'value': 1920,
            'default': 'True if empty() else будет значение из БД',
        },
        'video_read_height': {
            'text': 'разрешение входного видео (высота)',
            'value': 1080,
            'default': 'True if empty() else будет значение из БД',
        },
        'fps': {
            'text': 'FPS',
            'value': 10,
            'default': 'True if empty() else будет значение из БД',
        },
        'det_size_X': {
            'text': 'сжатие для insightface (ширина)',
            'value': 256,
            'default': 'True if empty() else будет значение из БД',
        },
        'det_size_Y': {
            'text': 'сжатие для insightface (высота)',
            'value': 256,
            'default': 'True if empty() else будет значение из БД',
        },
        'scale_percent': {
            'text': 'процент сжатия входного кадра (1/2) (1/3) и т.п',
            'value': (1 / 1),
            'default': 'True if empty() else будет значение из БД',
        },

    },
}
