const handleClick = (e) => {
  const btns = ['левая', 'средняя', 'правая'];
  const div = document.getElementById('div');
  const info = document.getElementById('info');
  info.style.left = e.clientX + 'px';
  info.style.top = e.clientY + 'px';
  info.innerHTML = `
  X = ${e.clientX}, Y = ${e.clientY} <br/>
  Нажата ${btns[e.button]} кнопка мыши
  `;
};
