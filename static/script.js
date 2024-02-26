document.addEventListener('DOMContentLoaded', function (event) {





    let slideDown_face = (target, duration = 500) => {
        document.querySelector('.info_camera').innerHTML = `
    <form>
        <label>Настройки интерфейса</label><br>
        <label for="demo_gui_on_full_screen_without_borders" id="demo_gui_title">Demo_gui_on_full_screen_without_borders:</label>
        <p>True <input type="checkbox" id="demo_gui_True"  </p>
        <p>False <input type="checkbox" id="demo_gui_False"  </p>
        
        <br>
        <label for="demo_monitor_index" id="demo_monitor_index_title">Demo_monitor_index:</label>
        <input type="number" id="demo_monitor_index_value"><br>

        <label for="face_rectangle_border_size" id="face_rectangle_border_size_title">Face_rectangle_border_size:</label>
        <input type="number" id="face_rectangle_border_size_value"><br>
    </form>`
        target.style.removeProperty('display');
        let display = window.getComputedStyle(target).display;
        if (display === 'none')
            display = 'block';

        target.style.display = display;
        let height = target.offsetHeight;
        target.style.overflow = 'hidden';
        target.style.height = 0;
        target.style.paddingTop = 0;
        target.style.paddingBottom = 0;
        target.style.marginTop = 0;
        target.style.marginBottom = 0;
        target.offsetHeight;
        target.style.boxSizing = 'border-box';
        target.style.transitionProperty = "height, margin, padding";
        target.style.transitionDuration = duration + 'ms';
        target.style.height = height + 'px';
        target.style.removeProperty('padding-top');
        target.style.removeProperty('padding-bottom');
        target.style.removeProperty('margin-top');
        target.style.removeProperty('margin-bottom');
        window.setTimeout(() => {
            target.style.removeProperty('height');
            target.style.removeProperty('overflow');
            target.style.removeProperty('transition-duration');
            target.style.removeProperty('transition-property');
        }, duration);
    }

    let slideDown_camera = (target, duration = 500) => {
        document.querySelector('.info_camera').innerHTML = `
    <form>
        <label>Настройки камеры</label><br>
        <label for="video_path_value" id="video_path_title">Video Path:</label>
        <input type="text" id="video_path_value"><br>


        <label for="video_read_width_value" id="video_read_width_title">Video Read Width:</label>
        <input type="number" id="video_read_width_value"><br>

        <label for="video_read_height" id="video_read_height_title">Video Read Height:</label>
        <input type="number" id="video_read_height_value"><br>

        <label for="fps">FPS:</label>
        <input type="number" id="fps_value"><br>

        <div>
            <label for="det_size_x" id="det_size_x_title">Detection Size X:</label>
            <input type="text" id="det_size_x_value"><br>
        </div>

        <div>
            <label for="det_size_y" id="det_size_y_title">Detection Size Y:</label>
            <input type="text" id="det_size_y_value"><br>
        </div>


        <label for="scale_percent" id="scale_percent_title">Scale Percent:</label>
        <input type="text" id="scale_percent_value" <br>
    </form>`
        target.style.removeProperty('display');
        let display = window.getComputedStyle(target).display;

        if (display === 'none')
            display = 'block';

        target.style.display = display;
        let height = target.offsetHeight;
        target.style.overflow = 'hidden';
        target.style.height = 0;
        target.style.paddingTop = 0;
        target.style.paddingBottom = 0;
        target.style.marginTop = 0;
        target.style.marginBottom = 0;
        target.offsetHeight;
        target.style.boxSizing = 'border-box';
        target.style.transitionProperty = "height, margin, padding";
        target.style.transitionDuration = duration + 'ms';
        target.style.height = height + 'px';
        target.style.removeProperty('padding-top');
        target.style.removeProperty('padding-bottom');
        target.style.removeProperty('margin-top');
        target.style.removeProperty('margin-bottom');

        window.setTimeout(() => {
            target.style.removeProperty('height');
            target.style.removeProperty('overflow');
            target.style.removeProperty('transition-duration');
            target.style.removeProperty('transition-property');
        }, duration);
    }
    let speedAnimation = 500;
    let targetId = document.getElementById("target");

    let slideBtnClick = (id, sl) => document.getElementById(id).addEventListener('click', () => sl(targetId, speedAnimation));

    slideBtnClick('triggerUp', slideDown_face);
    slideBtnClick('triggerDown', slideDown_camera);
    slideBtnClick('triggerToggle', slideDown_camera);

    // АПИХА

    let full_url_element = document.getElementById('full-url');
    let full_url = full_url_element.getAttribute('data-full-url');

    document.getElementById('triggerUp').addEventListener('click', function () {
        // настройки ИНТЕРФЕЙСА
        fetch(full_url)
            .then(response => response.json())
            .then(data => {
                let demo_gui = data['interface']['demo_gui_on_full_screen_without_borders']['value'][0]
                if (demo_gui === true) {
                    document.getElementById('demo_gui_True').checked = true;
                    document.getElementById('demo_gui_False').checked = false;
                } else {
                    document.getElementById('demo_gui_True').checked = false;
                    document.getElementById('demo_gui_False').checked = true;
                }
                document.getElementById('demo_gui_title').innerText = data['interface']['demo_gui_on_full_screen_without_borders']['text']
                document.getElementById('demo_monitor_index_title').innerText = data['interface']['demo_monitor_index']['text']
                document.getElementById('demo_monitor_index_value').value = data['interface']['demo_monitor_index']['value']
                document.getElementById('face_rectangle_border_size_title').innerText = data['interface']['face_rectangle_border_size']['text']
                document.getElementById('face_rectangle_border_size_value').value = data['interface']['face_rectangle_border_size']['value']
            })
    })
    document.getElementById('triggerDown').addEventListener('click', function () {
        // настроки КАМЕРЫ
        fetch(full_url)
            .then(response => response.json())
            .then(data => {
                document.getElementById('video_path_title').innerText = data['camera']['video_path']['text']
                document.getElementById('video_path_value').value = data['camera']['video_path']['value']
                document.getElementById('video_read_width_title').innerText = data['camera']['video_read_width']['text']
                document.getElementById('video_read_width_value').value = data['camera']['video_read_width']['value']
                document.getElementById('video_read_height_title').innerText = data['camera']['video_read_height']['text']
                document.getElementById('video_read_height_value').value = data['camera']['video_read_height']['value']
                document.getElementById('fps_value').value = data['camera']['fps']['value']
                document.getElementById('det_size_x_title').innerText = data['camera']['det_size_x']['text']
                document.getElementById('det_size_x_value').value = data['camera']['det_size_x']['value']
                document.getElementById('det_size_y_title').innerText = data['camera']['det_size_y']['text']
                document.getElementById('det_size_y_value').value = data['camera']['det_size_y']['value']
                document.getElementById('scale_percent_title').innerText = data['camera']['scale_percent']['text']
                document.getElementById('scale_percent_value').value = data['camera']['scale_percent']['value']


            })
    })
    function createStartButton(container) {
        container.innerHTML = '<button id="start">Старт</button>';
        let startButton = document.getElementById('start');
        startButton.style.backgroundColor = 'aquamarine'
        startButton.addEventListener('click', function () {
            createStopButton(container)

            let url_for_post_element = document.getElementById('url-for-post');
            let url_for_post = url_for_post_element.getAttribute('data-url-for-post');

            let data = {
                'video_path': +document.getElementById('video_path_value').value,
                'video_read_width': +document.getElementById('video_read_width_value').value,
                'video_read_height': +document.getElementById('video_read_height_value').value,
                'fps': +document.getElementById('fps_value').value,
                'det_size_x': +document.getElementById('det_size_x_value').value,
                'det_size_y': +document.getElementById('det_size_y_value').value,
                // 'scale_percent': eval(document.getElementById('scale_percent_value').value),
                // 'demo_monitor_index': +document.getElementById('demo_monitor_index_value').value,
                // 'face_rectangle_border_size': +document.getElementById('face_rectangle_border_size_value').value,
            };

            fetch(url_for_post, {
                "method": "POST",
                "headers": {"Content-Type": "application/json"},
                "body": JSON.stringify(data),
            })
                .then(response => {
                    return response.json();
                })


        });
    }

    function createStopButton(container) {
        container.innerHTML = '<button id="stop_btn">Стоп</button>';
        let stopButton = document.getElementById('stop_btn');
        stopButton.addEventListener('click', function () {

            createStartButton(container);
        });
    }

    let stopButtonContainer = document.querySelector('.stop');
    if (stopButtonContainer) {
        createStartButton(stopButtonContainer);
    }


})