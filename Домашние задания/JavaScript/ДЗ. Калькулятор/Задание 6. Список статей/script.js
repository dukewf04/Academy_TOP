window.addEventListener('scroll', () => {
  const scrollTop = window.scrollY;
  if (scrollTop > 100) {
    upButton.style.setProperty('visibility', 'visible');
    upButton.style.setProperty('right', '40px');
    upButton.style.setProperty('bottom', `-${scrollTop - 10}px`);
  } else {
    upButton.style.setProperty('visibility', 'hidden');
  }
});

upButton.onmousedown = () => {
  window.scrollTo(0, 0);
};
