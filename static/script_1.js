document.addEventListener('DOMContentLoaded', function (event) {

    let inner = document.querySelector('.inner');
    let form = document.querySelector('form');
    let duration = 500;
    let full_url_element = document.getElementById('full-url');
    let full_url = full_url_element.getAttribute('data-full-url');
    fetch(full_url)
        .then(response => response.json())
        .then(data => {
            // отрисовали кнопки
            for (let firstParam in data) {
                console.log(firstParam)
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

                // for (let second_param in data[firstParam]) {
                //     let label = document.createElement('label');
                //     label.textContent = data[firstParam][second_param]['text'];
                //
                //     let input = document.createElement('input');
                //     input.setAttribute('type', data[firstParam][second_param]['data_type']);
                //     input.value = data[firstParam][second_param]['value'];
                //
                //     div.append(label);
                //     div.append(input);
                // }

                divContainer.append(div);

                // let div = document.createElement('div');
                // div.classList.add('field');
                // div.id = firstParam
                // let divContainer = document.querySelector('form');
                // let title = document.createElement('p')
                // title.textContent = firstParam
                // div.append(title)
                // divContainer.append(div);
                // for (let second_param in data[firstParam]) {
                //     console.log(second_param)
                //     console.log(data[firstParam][second_param]['text'])
                //     console.log(data[firstParam][second_param]['data_type'])
                //     console.log(data[firstParam][second_param]['value'])
                //
                //
                //
                // }

            }
            let buttons = document.querySelectorAll('.buttons button');
            buttons.forEach(function (button) {
                button.addEventListener('click', function (e) {
                    animate();
                    let button = e.target
                    document.querySelectorAll('.buttons button').forEach(function (e) {
                        let form_div = document.getElementById(e.dataset.div)
                        form_div.classList.add('hide')
                        form_div.classList.remove('show')

                    })
                    document.getElementById(button.dataset.div).classList.add('show')
                });
            })


        });

    function animate() {
        inner.style.height = '0';
        setTimeout(function () {
            document.querySelector('form').style.display = 'block';
            inner.style.height = form.offsetHeight + 'px';
        }, duration);
    }

});
