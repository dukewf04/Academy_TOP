// Задание 1
var input = document.querySelector("#name");
function handleInput(e) {
  if (e.key >= "0" && e.key <= "9") {
    e.preventDefault();
  }
}

// Задание 2
const modal = document.querySelector(".t2-wrapper");
function handleOpenModal() {
  modal.style.setProperty("display", "flex");
}

function handleCloseModal() {
  modal.style.setProperty("display", "none");
}

// Задание 4
let lightNumber = 0;
const red = document.querySelector(".t4-red");
const yellow = document.querySelector(".t4-yellow");
const green = document.querySelector(".t4-green");
function handleChangeLight() {
  lightNumber = (lightNumber + 1) % 3;
  red.style.backgroundColor = lightNumber === 0 ? "red" : "gray";
  yellow.style.backgroundColor = lightNumber === 1 ? "yellow" : "gray";
  green.style.backgroundColor = lightNumber === 2 ? "green" : "gray";
}
