let slideDown_face = (target, duration = 500) => {
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
    document.querySelector('.info_camera').innerHTML = `
    <form>
        <label>Настройки интерфейса</label><br>
        <label for="demo_gui_on_full_screen_without_borders">Demo_gui_on_full_screen_without_borders:</label>
        <p>True <input type="checkbox" id="demo_gui_on_full_screen_without_borders" checked value="True" <br></p>
        <p>False <input type="checkbox" id="demo_gui_on_full_screen_without_borders" value="Fasle" <br></p>
        
        <br>
        <label for="demo_monitor_index">Demo_monitor_index:</label>
        <input type="number" id="demo_monitor_index" name="demo_monitor_index" value="123"><br>

        <label for="face_rectangle_border_size">Face_rectangle_border_size:</label>
        <input type="number" id="face_rectangle_border_size" name="face_rectangle_border_size" value="123"><br>

        

        <input type="button" id="saveButton" value="Сохранить" onclick="saveCameraSettings()">
    </form>`
    window.setTimeout(() => {
        target.style.removeProperty('height');
        target.style.removeProperty('overflow');
        target.style.removeProperty('transition-duration');
        target.style.removeProperty('transition-property');
    }, duration);
}

let slideDown_camera = (target, duration = 500) => {
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
    document.querySelector('.info_camera').innerHTML = `
    <form>
        <label>Настройки камеры</label><br>
        <label for="video_path">Video Path:</label>
        <input type="text" id="video_path" name="video_path" value="123"><br>

        <label for="video_read_width">Video Read Width:</label>
        <input type="number" id="video_read_width" name="video_read_width" value="123"><br>

        <label for="video_read_height">Video Read Height:</label>
        <input type="number" id="video_read_height" name="video_read_height" value="123"><br>

        <label for="fps">FPS:</label>
        <input type="number" id="fps" name="fps" value="123"><br>

        <label for="det_size_x">Detection Size X:</label>
        <input type="text" id="det_size_x" name="det_size_x" value="123"><br>

        <label for="det_size_y">Detection Size Y:</label>
        <input type="text" id="det_size_y" name="det_size_y" value="123"><br>

        <label for="scale_percent">Scale Percent:</label>
        <input type="number" id="scale_percent" name="scale_percent" value="123"><br>

        <input type="button" id="saveButton" value="Сохранить">
    </form>`
    window.setTimeout(() => {
        target.style.removeProperty('height');
        target.style.removeProperty('overflow');
        target.style.removeProperty('transition-duration');
        target.style.removeProperty('transition-property');
    }, duration);
}
let slideToggle = (target, duration = 500) => {
    if (window.getComputedStyle(target).display === 'none') {
        return slideDown_face(target, duration);
    } else {
        return slideDown_camera(target, duration);
    }
}

// ====

let speedAnimation = 400;
let targetId = document.getElementById("target");

let slideBtnClick = (id, sl) => document.getElementById(id).addEventListener('click', () => sl(targetId, speedAnimation));

slideBtnClick('triggerUp', slideDown_face);
slideBtnClick('triggerDown', slideDown_camera);
slideBtnClick('triggerToggle', slideToggle);
