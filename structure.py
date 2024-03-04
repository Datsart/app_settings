def settings_dict():
    settings_dictionary = {
        'interface': {
            'demo_gui_on_full_screen_without_borders': {
                'text': 'Отображать на весь экран без границы:',
                'value': [True, False],
                'default': 'True if empty() else будет значение из БД',
            },
            'demo_monitor_index': {
                'text': 'Индекс монитора:',
                'value': 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'face_rectangle_border_size': {
                'text': 'Толщина обводки найденного лица:',
                'value': 3,
                'default': 'True if empty() else будет значение из БД',
            }
        },
        'camera': {
            'video_path': {
                'text': 'Rtsp адрес или индекс вебкамеры:',
                'value': 0,
                'default': 'True if empty() else будет значение из БД',
            },
            'video_read_width': {
                'text': 'Разрешение входного видео (ширина):',
                'value': 1920,
                'default': 'True if empty() else будет значение из БД',
            },
            'video_read_height': {
                'text': 'разрешение входного видео (высота):',
                'value': 1080,
                'default': 'True if empty() else будет значение из БД',
            },
            'fps': {
                'text': 'FPS:',
                'value': 10,
                'default': 'True if empty() else будет значение из БД',
            },
            'det_size_x': {
                'text': 'Сжатие для insightface (ширина):',
                'value': 256,
                'default': 'True if empty() else будет значение из БД',
            },
            'det_size_y': {
                'text': 'Сжатие для insightface (высота):',
                'value': 256,
                'default': 'True if empty() else будет значение из БД',
            },
            'scale_percent': {
                'text': 'Процент сжатия входного кадра (1/2) (1/3) и т.п:',
                'value': '(1 / 1)',
                'default': 'True if empty() else будет значение из БД',
            },
        },
    }
    return settings_dictionary


def get_settings_info(settings_dict):
    for category, parameters in settings_dict.items():
        # print(f"Категория: {category}")
        for parameter, info in parameters.items():
            text = info['text']
            value = info['value']
            print(f"Категория: {category}")
            print(f"  Параметр: {parameter}")
            print(f"    Описание: {text}")
            print(f"    Значение: {value}")
            print("")


# Получаем словарь настроек
settings = settings_dict()

# Выводим информацию о настройках
# get_settings_info(settings)
for i in settings:
    for j in settings[i]:
        print(j)
