document.addEventListener('DOMContentLoaded', function (event) {


    function createStartButton(container) {
        container.innerHTML = '<button id="start">Старт</button>';
        let startButton = document.getElementById('start');
        startButton.style.backgroundColor = 'aquamarine'
        startButton.addEventListener('click', function () {

            createStopButton(container)
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
        <label for="video_path" id="video_path_title">Video Path:</label>
        <input type="text" id="video_path_value"><br>

        <label for="video_read_width" id="video_read_width_title">Video Read Width:</label>
        <input type="number" id="video_read_width_value"><br>

        <label for="video_read_height" id="video_read_height_title">Video Read Height:</label>
        <input type="number" id="video_read_height_value"><br>

        <label for="fps">FPS:</label>
        <input type="number" id="fps_value"><br>

        <label for="det_size_x" id="det_size_x_title">Detection Size X:</label>
        <input type="text" id="det_size_x_value" <br>

        <label for="det_size_y" id="det_size_y_title">Detection Size Y:</label>
        <input type="text" id="det_size_y_value" <br>

        <label for="scale_percent" id="scale_percent_title">Scale Percent:</label>
        <input type="number" id="scale_percent_value" <br>
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
    let full_url_element = document.getElementById('full-url');
    let full_url = full_url_element.getAttribute('data-full-url');

    // console.log("Full URL in JavaScript:", full_url);
    document.getElementById('triggerUp').addEventListener('click', function () {
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
                // document.getElementById('video_path_title').innerText = data['camera']['video_path']['text']
                // document.getElementById('video_path_value').value = data['camera']['video_path']['value']
                console.log(document.getElementById('video_path_title'))
            })
    })

})