let button = document.querySelector('.button');
let button2 = document.querySelector('.button2');

let inner = document.querySelector('.inner');
let form = document.querySelector('form')
let duration = 500

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