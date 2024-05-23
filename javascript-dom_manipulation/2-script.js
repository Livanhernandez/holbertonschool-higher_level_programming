const redHeaderButton = document.getElementById('redHeaderButton');


redHeaderButton.addEventListener('click', function() {
    const headerElement = document.querySelector('header');
    headerElement.classList.add('red');
});
