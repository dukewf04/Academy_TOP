// Задание 6
const ball = document.querySelector('#ball');

const handleClick = (e) => {
  const field = document.querySelector('#field').getBoundingClientRect();
  let moveX = e.clientX;
  if (moveX < field.left) {
    moveX = field.left;
  } else if (moveX > field.left + field.width) {
    moveX = field.left + field.width - 70;
  } else {
    moveX -= 35;
  }

  let moveY = e.clientY;
  if (moveY < field.top) {
    moveY = field.top;
  } else if (moveY > field.top + field.height) {
    moveY = field.top + field.height - 70;
  } else {
    moveY -= 35;
  }

  ball.style.setProperty('left', `${moveX}px`);
  ball.style.setProperty('top', `${moveY}px`);
};
