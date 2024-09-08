// Правильные ответы
const correctAnswers = [5, 5];

const getCookies = () => {
  let x = document.cookie;
  let s = x.split('; ');
  let cookieObject = {};
  var c;
  for (let i = 0; i < s.length; i++) {
    c = s[i].split('=');
    cookieObject[c[0]] = c[1];
  }

  return cookieObject;
};

const onLoad = () => {
  const cookieObject = getCookies();

  if ('superStyle' in cookieObject) {
    const style = JSON.parse(cookieObject['superStyle']);
    resultText.style.setProperty('font-weight', style.bold);
    resultText.style.setProperty('text-decoration', style.underline);
    resultText.style.setProperty('font-style', style.italic);
    resultText.style.setProperty('text-align', style.alignment);
    resultText.innerHTML = style.text;
  }
};

show.onclick = () => {
  const bold = document.querySelector('input[id="bold"]:checked');
  const underline = document.querySelector('input[id="underline"]:checked');
  const italic = document.querySelector('input[id="italic"]:checked');
  const alignment = document.querySelector('input[name="alignment"]:checked');

  const obj = {
    bold: bold ? bold.value : '',
    underline: underline ? underline.value : '',
    italic: italic ? italic.value : '',
    alignment: alignment ? alignment.value : '',
    text: text.value,
  };

  document.cookie = `superStyle=${JSON.stringify(obj)};path=/`;
};
