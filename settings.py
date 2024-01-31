class Settings:
    # не выводить обводку bbox для лиц у которых "корона"
    not_show_rectangle_if_crown = False
    # отображать "корону" над bbox
    crown = False
    # список персон с "короной"
    crown_persons = []

    # Камера
    # video_path = 'rtsp://admin:1qaz2wsx@185.78.93.161'
    # video_path = 'istockphoto-1357364144-640_adpp_is.mp4'
    video_path = 0  # rtsp адрес или индекс вебкамеры
    video_read_width, video_read_height = 1920, 1080  # Разрешение входного видео
    fps = 10
    det_size = (256, 256)  # сжатие для insightface
    scale_percent = (1 / 1)  # процент сжатия входного кадра (1/2) (1/3) и т.п

    # Интерфейс
    demo_gui_on_full_screen_without_borders = False  # True - запуск во весь экран без рамок; False - с рамками
    demo_monitor_index = 0
    face_rectangle_border_size = 3  # толщина обводки найденного лица

    # SSH
    receive_data_from_ftp = True  # Получать ли данные с сервера

    # Путь к датасету
    path = 'Dataset'

    # Схожесть
    threshold_similarity = 0.5  # Трешхолд схожести лиц - чем меньше тем больше похожи (от 0 до 1)
    method_calculate_coef_compare = 'SoloAndFamily'  # Методы обнаружения похожего юзера (FirstRecord, MeanCoef,SoloAndFamily)

    # Мини модель
    use_temp_model = True  # Использовать ли мини модель в оперативной памяти
    interval_update_temp_model = 10  # Интервал обновления мини модели (в секундах)

    # Обогащение датасета с камеры
    add_user_from_camera = True  # Обогащать ли датасет юзеров фотографиями с камеры
    threshold_add_photo = 0.4  # Трешхолд схожести лиц для обогащения - чем меньше тем больше похожи (от 0 до 1)
    interval_add_photo_minute = 0.1  # Интервал добавления фото (в минутах)
    cnt_max_photo = 5  # Максимальное кол-во фото у юзера

    # Создание датасета
    detect_only_big_face_create_dataset = True  # Брать только наибольшие лица при создании датасета

    # Логирование
    interval_session_minute = 0.2  # Интервал логирования посещений юзера

    # Фильтры обнаружения лица
    filter_size = [None, None]  # Фильтр на размер лица
    filter_proba_face = 0.5  # Вероятность того что найдено лицо
    round_proba_face = False
    use_priority = True
    use_events_vip = True

    # Настройки для подключения к серверу
    server_host = ''  # ip адрес
    server_port = 22
    server_username = ''
    server_password = ''
    server_path_img = ''
    server_use_command_tree = False  # использовать команду tree для просмотра файлов на сервере

    # Инициализация путей
    path_images = f"{path}/images"
    path_faces = f"{path}/faces"
    path_dict_info_valid = f'{path_faces}/dict_info_valid.pkl'
    path_db = f"{path_faces}/data.db"

    # Инициализация имен таблиц в бд
    table_face_info = 'face_info'
    table_model = 'model'
    table_valid_user = 'user_valid'
    table_session_user = 'user_session'
    table_processed_img = 'processed_img'


