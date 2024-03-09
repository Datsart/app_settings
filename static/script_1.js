document.addEventListener('DOMContentLoaded', function (event) {


    let inner = document.querySelector('.inner');
    let form = document.querySelector('form')
    let duration = 500
    let full_url_element = document.getElementById('full-url');
    let full_url = full_url_element.getAttribute('data-full-url');

    fetch(full_url)
        .then(response => response.json())
        .then(data => {
            // отрисовали кнопки
            for (fist_param in data) {
                let button = document.createElement('button')
                button.textContent = fist_param
                let buttonsContainer = document.querySelector('.buttons');

                buttonsContainer.appendChild(button);

                console.log(document.querySelector('.buttons'))
            }
        })

    function animate() {
        inner.style.height = '0'
        setTimeout(function () {
            document.querySelector('form').style.display = 'block'
            inner.style.height = form.offsetHeight + 'px'
        }, duration)

    }

// Добавляем обработчик события на клик по кнопке
    button.addEventListener('click', function () {

        animate()
        setTimeout(function () {
            // формы и поля
        }, duration)

    })
    button2.addEventListener('click', function () {
        animate()
        setTimeout(function () {
            // формы и поля
        }, duration)


    })
})