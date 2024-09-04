// Задание 1
t1_plus.onclick = () => {
  t1_number.innerText = +t1_number.innerText + 1;
};

t1_minus.onclick = () => {
  t1_number.innerText = +t1_number.innerText - 1;
};

// Задание 2
const rc = () => {
  return `rgb(${Math.random() * 255},${Math.random() * 255},${Math.random() * 255})`;
};
let colorsBlock = document.getElementsByClassName('t2_colors')[0];
t2_add_block.onclick = () => {
  const newBlock = document.createElement('div');
  newBlock.classList.add('t2ColorBlock');
  newBlock.style.backgroundColor = rc();
  colorsBlock.appendChild(newBlock);
  newBlock.addEventListener('click', () => {
    colorsBlock.removeChild(newBlock);
  });
};

// Задание 3
t3ColorPicker.addEventListener('change', () => {
  t3Text.style.color = t3ColorPicker.value;
});

// Задание 4
t4AddComment.addEventListener('click', () => {
  const d = new Date();
  t4Comments.innerHTML += `
    <b>${t4Name.value}</b><br>
    ${d.getDay()}.${d.getMonth()}.${d.getFullYear()}<br>
    ${t4Comment.value}<br><hr>
    `;
});

// Задание 5
const countries = [
  'Россия',
  'Италия',
  'Армения',
  'Белорусия',
  'Чехия',
  'Германия',
  'Франция',
  'Португалия',
  'Эфиопия',
  'Турция',
];

const addCountry = (e) => {
  t5Input.value = e.target.innerText;
};

t5Input.addEventListener('input', () => {
  if (t5Input.value === '') {
    t5Countries.innerHTML = '';
    return;
  }
  const filteredArr = countries.filter(
    (item) => item.toLowerCase().indexOf(t5Input.value.toLowerCase()) !== -1,
  );

  let filteredCountries = '';
  filteredArr.forEach((country) => {
    filteredCountries += `
      <li onclick="addCountry(event)">${country}</li>
    `;
  });
  t5Countries.innerHTML = filteredCountries;
});
