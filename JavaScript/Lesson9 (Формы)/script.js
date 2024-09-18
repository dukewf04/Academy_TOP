//Регулярные выражения
// \d - любая цифра, \s - пробельный символ, \w - большая или малькая буква, .(точка) - любой символ, \D - не цифра, \S -не пробел, \W- не символ, \x - не цифра(цифра, буква)
// [0-9], [a-z],[a-я], [А-Я],[A-Z]
//[^1-3] - не должны находится, ставим степень
// ? - 0 или 1 раз,
// +(плюс) - 1 и более раз,
// * - n символов
// {2} - ровно 2 повтора, {2,7} - от 2 до 7 повторов
// Например: "\d{7}" - семь цифр подрят, "\s+" - один или более пробельный символ
// для отображения спец. символа: "/$/"
var templateName = /^[a-z]*$/;
var templatePhone = /^\+\d{12}$/;
var templateLogin = /^[A-Z][a-z]*$/;
function checkForm() {
  //обработка имени пользователя
  var nameText = document.getElementById('name').value;
  var loginText = document.getElementById('login').value;
  var passwordText = document.getElementById('password').value;
  var phoneText = document.getElementById('ph').value;
  if (templateName.exec(nameText)) {
    alert('Неверное имя');
    return false;
  }
  //обработка логина
  if (templateLogin.exec(loginText)) {
    alert('Неверный логин');
    return false;
  }
  //обработка пароля
  if (passwordText.lenght < 6) {
    alert('Неверный пароль');
    return false;
  }
  if (templatePhone.exec(phoneText)) {
    alert('Неверный номер телефона');
    return false;
  }

  // Создание формы регистрации на основе cookie
  var expDate = new Date();
  expDate.setTime(expDate.getTime() + 60 * 1000);
  document.cookie = `registered=${nameText};expires=${expDate.toGMTString()};path=/`;
  return true;
}

const checkReg = () => {
  let x = document.cookie;
  let s = x.split(';');
  let cookieObject = {};
  let c;
  for (var i = 0; i < s.length; i++) {
    c = s[i].split('=');
    cookieObject[c[0]] = c[1];
  }

  if ('registered' in cookieObject) {
    regDiv.innerHTML = `Hello ${cookieObject['registered']}`;
  }

  // Добавление cookie-файлов в проект
  // document.cookie =
  //   "registered='User'; expires='Mon', 09 sep 2024 18:38:40 GMT; path=/";

  // window.out.innerHTML = document.cookie;
  // registered - это имя пользователя
  // expires - срок действия куки-файлов
  // path - Облать действия куки
  // domain - имя сайта (сервера), отправившего данную страницу
  // secure - протокол шифрования
  // document.cookie - получить все параметры для создания и заполнения
  // До 300 cookie файлов
  // от 1 домена(сайта) можно хранить до 20 значений.
};
