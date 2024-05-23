// First, we grab the element by its ID "red_header".
const redHeaderElement = document.getElementById('red_header');

// Then, we add an event listener for the "click" event.
redHeaderElement.addEventListener('click', function() {
  // Upon clicking, this function is executed, selecting the header element.
  const headerElement = document.querySelector('header');
  
  // The color of the header element's text is changed to red (#FF0000).
  headerElement.style.color = '#FF0000';
});
