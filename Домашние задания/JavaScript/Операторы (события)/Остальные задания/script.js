// Задание 1
var input = document.querySelector('#name');
function handleInput(e) {
  if (e.key >= '0' && e.key <= '9') {
    e.preventDefault();
  }
}

// Задание 2
const modal = document.querySelector('.t2-wrapper');
function handleOpenModal() {
  modal.style.setProperty('display', 'flex');
}

function handleCloseModal() {
  modal.style.setProperty('display', 'none');
}

// Задание 4
let lightNumber = 0;
const red = document.querySelector('.t4-red');
const yellow = document.querySelector('.t4-yellow');
const green = document.querySelector('.t4-green');
function handleChangeLight() {
  lightNumber = lightNumber === 2 ? 0 : lightNumber + 1;
  switch (lightNumber) {
    case 0:
      red.style.backgroundColor = 'red';
      yellow.style.backgroundColor = 'gray';
      green.style.backgroundColor = 'gray';
      break;
    case 1:
      red.style.backgroundColor = 'gray';
      yellow.style.backgroundColor = 'yellow';
      green.style.backgroundColor = 'gray';
      break;
    case 2:
      red.style.backgroundColor = 'gray';
      yellow.style.backgroundColor = 'gray';
      green.style.backgroundColor = 'green';
  }
}