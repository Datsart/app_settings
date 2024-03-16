def settings_dict():
    from app import get_value_by_text
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
