// Задание 1
const handleClick = (e) => {
  const el = document.getElementById('t1-number');
  el.innerText = Math.floor(100 * (1 - Math.random()));
};

// Задание 3
const handleClickShow = () => {
  const el = document.querySelector('.t3-content');
  const computedStyle = window.getComputedStyle(el);
  const displayStyle = computedStyle.getPropertyValue('display');
  el.style.setProperty('display', displayStyle === 'none' ? 'block' : 'none');
};

// Задание 4
const textList = ['HTML forever!', 'CSS forever!', 'JS forever!'];
const sidebarItems = document.querySelectorAll('.t2-sidebar-item');
const content = document.querySelector('.t2-content');
sidebarItems.forEach((element) => {
  element.addEventListener('mousedown', () => {
    const index = element.id.indexOf('_') + 1;
    content.innerText = textList[element.id.slice(Number(index))];
  });
});

// Задание 5
const buttons = document.querySelectorAll('.t5-container button');
buttons.forEach((element) => {
  element.addEventListener('mousedown', () => {
    const index = element.id.indexOf('_') + 1;
    const blockId = element.id.slice(index);
    const el = document.getElementById(`t5-${blockId}`);
    el.style.display = 'none';
  });
});

// Задание 6
var progressBarWidth = 0;
const handleAddProgressBar = (e) => {
  const bar = document.getElementById('t6-bar');
  const barWidth = bar.getBoundingClientRect().width;
  const el = document.getElementById('t6-bar-progress');  
  progressBarWidth += barWidth / 100 * 5
  if (progressBarWidth >= barWidth) {
    progressBarWidth = barWidth
  }
  el.style.setProperty('width', `${progressBarWidth}px`)
};
