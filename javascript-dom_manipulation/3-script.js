// Select the element with the ID 'toggle_header'.
const toggleHeaderButton = document.getElementById('toggle_header');


toggleHeaderButton.addEventListener('click', function() {
  const headerElement = document.querySelector('header');

  if (headerElement.classList.contains('green')) {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  } else {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  }
});
