document.querySelectorAll('button:not(.equal, .clear)').forEach((item) => {
  item.addEventListener('click', (e) => {
    if (display.innerText === '0') display.innerText = '';
    display.innerText += item.innerText;
  });
});

equal.onmousedown = () => {
  const result = eval(display.innerText);
  display.innerText = result !== Infinity ? result : display.innerText;
};

clear.onmousedown = () => {
  display.innerText = '0';
};
