// First, select the element with the ID 'add_item'.
const addItemButton = document.getElementById('add_item');


addItemButton.addEventListener('click', function() {
  const myList = document.querySelector('.my_list');

  const newLi = document.createElement('li');

  newLi.textContent = 'Item';

  myList.appendChild(newLi);
});
