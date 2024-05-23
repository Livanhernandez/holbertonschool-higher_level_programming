const updateHeaderButton = document.getElementById('update_header');


updateHeaderButton.addEventListener('click', function() {
  const headerElement = document.querySelector('header');

  headerElement.textContent = 'New Header!!!';
});
