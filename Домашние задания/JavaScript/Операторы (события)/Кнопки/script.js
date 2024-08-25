// Задание 6
const buttons = document.querySelectorAll('.tooltip');
buttons.forEach((button) => {
  const tooltipText = button.querySelector('.tooltipText');

  button.addEventListener('mouseover', (e) => {
    const buttonRect = button.getBoundingClientRect();
    const top = buttonRect.top;
    if (top < 45) {
      tooltipText.style.top = '130%';
      tooltipText.classList.add('tooltipTextBottom');
    }
  });
});
