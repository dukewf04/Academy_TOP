// Регулярные выражения
// \d - любая цифра, \s - пробельный символ, \w - большая или маленькая буква
// . - любой символ, \D - не цифра, \S - не пробел, \W - не символ
// \x - не цифра и не буква
// [0-9], [a-z], [а-я], [A-Z], [А-Я] - должны находиться
// [^1-3] - не должны находиться, ставим степень
// ? - 0 или 1 раз
// +(плюс) - 1 и более вхождений
// {2} - ровно 2 повтора, {2,7} - от 2 до 7 повторов
// Например: "\d{7}" - семь цифр подряд. "s+" - один или более пробельных символов
// Для отображения спец. символов: "/$/"
let templateName = /^[A-Z][a-z]*$/;
let templatePhone = /^\+\d{12}$/;
let templateLogin = /^[A-Z][a-z]*$/;
const checkForm = (e) => {
  let nameText = document.getElementById("name").value;
  let loginText = document.getElementById("login").value;
  let passwordText = document.getElementById("password").value;
  let phoneText = document.getElementById("ph").value;
  console.log(templateName.exec(nameText));
  if (!templateName.exec(nameText)) {
    alert("Неверное имя");
    return false;
  }
  if (!templateLogin.exec(loginText)) {
    alert("Неверный логин");
    return false;
  }
  if (!passwordText.length < 6) {
    alert("Неверный пароль");
    return false;
  }
  if (!templatePhone.exec(phoneText)) {
    alert("Неверный номер телефона");
    return false;
  }

  return true;
};
