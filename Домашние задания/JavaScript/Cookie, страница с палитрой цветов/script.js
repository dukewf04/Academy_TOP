function validateColorData(name, type, code) {
  let errors = {
    name: false,
    code: false,
  };

  if (name.trim() === '' || !/^[a-zA-Z]+$/.test(name)) {
    errors.name = 'Название должно быть заполнено буквенными символами';
  }

  let codeRegex;
  if (type === 'RGB') {
    codeRegex = /^([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3})$/;
  } else if (type === 'RGBA') {
    codeRegex = /^([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3}),([0-1]\.[0-9]{1,2})$/;
  } else if (type === 'HEX') {
    codeRegex = /^#[0-9A-Fa-f]{6}$/;
  }

  if (!codeRegex.test(code)) {
    errors.code = 'Неверный формат кода цвета';
  }

  return errors;
}

function addColor(name, type, code) {
  const colorItem = document.createElement('div');
  colorItem.classList.add('color-item');
  let color = '';
  switch (type) {
    case 'RGB':
      color = `RGB(${code})`;
      break;
    case 'RGBA':
      color = `RGBA(${code})`;
      break;
    case 'HEX':
      color = code;
  }
  colorItem.style.backgroundColor = color;
  colorItem.innerHTML = `${name}<br>${type}<br>${code}`;
  document.querySelector('.palette').appendChild(colorItem);
}

function getColorsFromCookie() {
  const colors = JSON.parse(
    document.cookie
      .split('; ')
      .find((row) => row.startsWith('colors='))
      ?.split('=')[1] || '[]',
  );
  return colors;
}

function saveColorsToCookie(colors) {
  document.cookie = `colors=${JSON.stringify(colors)}; max-age=${3 * 60 * 60}; path=/`;
}

const colors = getColorsFromCookie();
colors.forEach((color) => addColor(color.name, color.type, color.code));

const colorForm = document.getElementById('colorForm');
colorForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const type = document.getElementById('type').value;
  const code = document.getElementById('code').value;

  const errors = validateColorData(name, type, code);

  document.getElementById('nameError').textContent = errors.name || '';
  document.getElementById('codeError').textContent = errors.code || '';

  if (!errors.name && !errors.code) {
    addColor(name, type, code);

    const colors = getColorsFromCookie();
    colors.push({ name: name, type: type, code: code });
    saveColorsToCookie(colors);

    colorForm.reset();
  }
});
