let speedAnimation = 400;
let targetId = document.getElementById("target");
let triggerStop = document.getElementById("triggerStop");
let cameraSettingsForm = document.getElementById("cameraSettingsForm");

function slideUp(target, duration = 500) {
    target.style.transitionProperty = 'height, margin, padding';
    target.style.transitionDuration = duration + 'ms';
    target.style.boxSizing = 'border-box';
    target.style.height = target.offsetHeight + 'px';
    target.offsetHeight;
    target.style.overflow = 'hidden';
    target.style.height = 0;
    target.style.paddingTop = 0;
    target.style.paddingBottom = 0;
    target.style.marginTop = 0;
    target.style.marginBottom = 0;
    window.setTimeout(() => {
        target.style.display = 'none';
        target.style.removeProperty('height');
        target.style.removeProperty('padding-top');
        target.style.removeProperty('padding-bottom');
        target.style.removeProperty('margin-top');
        target.style.removeProperty('margin-bottom');
        target.style.removeProperty('overflow');
        target.style.removeProperty('transition-duration');
        target.style.removeProperty('transition-property');
    }, duration);
}

function slideDown(target, duration = 500) {
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

function slideToggle(target, duration = 500) {
    let display = window.getComputedStyle(target).display;
    if (display === 'none' || target.offsetHeight === 0) {
        target.style.display = 'flex'; // Изменено на flex
        target.style.height = 'auto';
        let height = target.offsetHeight;
        target.style.height = 0;
        window.setTimeout(() => {
            target.style.height = height + 'px';
        }, 0);
    } else {
        target.style.height = '0';
        window.setTimeout(() => {
            target.style.display = 'none';
        }, duration);
    }
}

function slideBtnClick(id, sl) {
    document.getElementById(id).addEventListener('click', function () {
        console.log(`Button ${id} clicked`);
        if (id === 'triggerUp') {
            slideToggle(cameraSettingsForm, speedAnimation);
        } else {
            sl(targetId, speedAnimation);
        }

        if (id === 'triggerStart') {
            triggerStop.style.display = 'block';
        } else if (id === 'triggerStop') {
            triggerStop.style.display = 'none';
        }
    });
}

slideBtnClick('triggerDown', slideDown);
slideBtnClick('triggerStart', slideToggle);
triggerStop.style.display = 'none';
slideBtnClick('triggerStop', slideUp);

function saveCameraSettings() {
    // Получение значений полей формы
    var video_path = document.getElementById('video_path').value;
    var video_read_width = document.getElementById('video_read_width').value;
    var video_read_height = document.getElementById('video_read_height').value;
    var fps = document.getElementById('fps').value;
    var det_size = document.getElementById('det_size').value;
    var scale_percent = document.getElementById('scale_percent').value;

    // Отправка данных на сервер (в данном случае, на ваш Flask-сервер)
    fetch('/save_settings', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            video_path: video_path,
            video_read_width: video_read_width,
            video_read_height: video_read_height,
            fps: fps,
            det_size: det_size,
            scale_percent: scale_percent,
        }),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Вместо вывода в консоль, вы можете выполнить дополнительные действия, например, обновить интерфейс
            // Здесь вы можете добавить закрытие формы
            slideUp(cameraSettingsForm, speedAnimation);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
// Обработчик для кнопки "Настройки камеры" в начале скрипта
slideBtnClick('triggerUp', slideToggle);
document.addEventListener('click', function (event) {
    var isClickInsideForm = cameraSettingsForm.contains(event.target);
    var isClickOnTriggerUp = document.getElementById('triggerUp').contains(event.target);

    if (!isClickInsideForm && !isClickOnTriggerUp) {
        // Если клик был вне формы и не на кнопке "Настройки камеры", то скрываем форму
        slideUp(cameraSettingsForm, speedAnimation);
    }
});

// Обработчик для кнопки "Сохранить"
document.getElementById('saveButton').addEventListener('click', saveCameraSettings);