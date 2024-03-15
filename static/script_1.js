document.addEventListener('DOMContentLoaded', function (event) {
    let form = document.querySelector('form');
    let inner = document.querySelector('.inner');
    let duration = 500;
    let full_url_element = document.getElementById('full-url');
    let full_url = full_url_element.getAttribute('data-full-url');
    fetch(full_url)
        .then(response => response.json())
        .then(data => {
            // отрисовали кнопки
            for (let firstParam in data) {
                let button = document.createElement('button');
                button.textContent = firstParam;
                button.classList.add('button_' + firstParam);
                button.dataset.div = firstParam
                let buttonsContainer = document.querySelector('.buttons');
                buttonsContainer.appendChild(button);

                // создаем класс ДИВОВ по первым основным параметрам
                let div = document.createElement('div');
                div.classList.add('field');
                div.id = firstParam;
                let divContainer = document.querySelector('form');
                let title = document.createElement('p');
                title.textContent = firstParam;
                div.append(title);
                for (let second_param in data[firstParam]) {
                    let fieldDiv = document.createElement('div');
                    fieldDiv.classList.add('field');

                    let label = document.createElement('label');
                    label.textContent = data[firstParam][second_param]['text'];

                    let input = document.createElement('input');
                    input.setAttribute('type', data[firstParam][second_param]['data_type']);
                    input.value = data[firstParam][second_param]['value'];

                    fieldDiv.append(label);
                    fieldDiv.append(input);

                    div.append(fieldDiv);
                }
                divContainer.append(div);
            }
            let buttons = document.querySelectorAll('.buttons button');
            buttons.forEach(function (button) {
                button.addEventListener('click', function (e) {
                    animate();
                    setTimeout(function () {
                        let button = e.target
                        document.querySelectorAll('.buttons button').forEach(function (e) {
                            let form_div = document.getElementById(e.dataset.div)
                            form_div.classList.add('hide')
                            form_div.classList.remove('show')
                        }, duration)
                        document.getElementById(button.dataset.div).classList.add('show')
                        setTimeout(function () {
                            inner.style.height = form.offsetHeight + 'px';
                        }, 0);
                    }, duration)
                });
            })
        });

    function animate() {
        inner.style.height = '0';
        setTimeout(function () {
            document.querySelector('form').style.display = 'block';
            setTimeout(function () {
                inner.style.height = form.offsetHeight + 'px';
            }, 0);
        }, 500);
    }

    function createStartButton(container) {
        container.innerHTML = '<button id="start">Старт</button>';
        let startButton = document.getElementById('start');
        startButton.style.backgroundColor = 'greenyellow'
        startButton.addEventListener('click', function () {
            createStopButton(container)

            let url_for_post_element = document.getElementById('url-for-post');
            let url_for_post = url_for_post_element.getAttribute('data-url-for-post');
            // то что я передаю обратно во фласк
            let data = {
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


});
