document.querySelectorAll('.tab').forEach((item) => {
  item.addEventListener('click', () => {
    item.querySelector('.subMenu').style.display = 'block';
  });

  item.addEventListener('mouseleave', () => {
    item.querySelector('.subMenu').style.display = 'none';
  });
});
