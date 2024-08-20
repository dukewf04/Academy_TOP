// 1. Определение возрастной группы
let age = prompt('Введите свой возраст:');

if (age >= 0 && age <= 2) {
  console.log('Ребенок');
} else if (age >= 12 && age <= 18) {
  console.log('Подросток');
} else if (age >= 18 && age <= 60) {
  console.log('Взрослый');
} else if (age >= 60) {
  console.log('Пенсионер');
} else {
  console.log('Некорректный возраст.');
}

// 2. Вывод спецсимвола по номеру клавиши
let number = prompt('Введите число от 0 до 9:');

switch (number) {
  case '1':
    console.log('!');
    break;
  case '2':
    console.log('@');
    break;
  case '3':
    console.log('#');
    break;
  case '4':
    console.log('$');
    break;
  case '5':
    console.log('%');
    break;
  case '6':
    console.log('^');
    break;
  case '7':
    console.log('&');
    break;
  case '8':
    console.log('');
    break;
  case '9':
    console.log('(');
    break;
  case '0':
    console.log(')');
    break;
  default:
    console.log('Некорректный ввод.');
}

// 3. Проверка на одинаковые цифры в трехзначном числе
let number3 = prompt('Введите трехзначное число:');

if (number3[0] === number3[1] || number3[0] === number3[2] || number3[1] === number3[2]) {
  console.log('В числе есть одинаковые цифры.');
} else {
  console.log('В числе нет одинаковых цифр.');
}

// 4. Проверка високосного года
let year = prompt('Введите год:');

let isLeapYear = year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);

if (isLeapYear) {
  console.log('Год ' + year + ' - високосный.');
} else {
  console.log('Год ' + year + ' - не високосный.');
}

// 5. Проверка палиндрома
let number5 = prompt('Введите пятиразрядное число:');

let isPalindrome = number5 === number5.split('').reverse().join('');

if (isPalindrome) {
  console.log('Число ' + number5 + ' - палиндром.');
} else {
  console.log('Число ' + number5 + ' - не палиндром.');
}

// 6. Конвертер валют
let usdAmount = prompt('Введите количество USD:');
let targetCurrency = prompt('В какую валюту перевести? (EUR, UAN, AZN):');

let convertedAmount;

switch (targetCurrency) {
  case 'EUR':
    convertedAmount = usdAmount * 0.92;
    break;
  case 'UAN':
    convertedAmount = usdAmount * 37.3;
    break;
  case 'AZN':
    convertedAmount = usdAmount * 1.7;
    break;
  default:
    console.log('Некорректная валюта.');
    return;
}

console.log('Сумма в ' + targetCurrency + ': ' + convertedAmount.toFixed(2));

// 7. Скидка на покупку
let purchaseAmount = prompt('Введите сумму покупки:');

let discount =
  purchaseAmount >= 500 ? 0.07 : purchaseAmount >= 300 ? 0.05 : purchaseAmount >= 200 ? 0.03 : 0;

let discountedAmount = purchaseAmount - purchaseAmount * discount;

console.log('Сумма к оплате со скидкой: ' + discountedAmount.toFixed(2));

// 8. Окружность в квадрате
let circleCircumference = prompt('Введите длину окружности:');
let squarePerimeter = prompt('Введите периметр квадрата:');

let circleRadius = circleCircumference / (2 * Math.PI);
let squareSide = squarePerimeter / 4;

let fits = circleRadius * 2 <= squareSide;

if (fits) {
  console.log('Окружность может поместиться в квадрат.');
} else {
  console.log('Окружность не может поместиться в квадрат.');
}

// 9. Викторина
let score = 0;

let question1 = prompt('Вопрос 1: ... (3 варианта ответа)');
if (question1 === 'Правильный ответ') {
  score += 2;
}

let question2 = prompt('Вопрос 2: ... (3 варианта ответа)');
if (question2 === 'Правильный ответ') {
  score += 2;
}

let question3 = prompt('Вопрос 3: ... (3 варианта ответа)');
if (question3 === 'Правильный ответ') {
  score += 2;
}

console.log('Вы набрали ' + score + ' баллов.');

// 10. Даты
function getNextDate(day, month, year) {
  const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;

  const daysInMonth = [31, 28 + (isLeapYear ? 1 : 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  day++;

  if (day > daysInMonth[month - 1]) {
    day = 1;
    month++;
  }

  if (month > 12) {
    month = 1;
    year++;
  }

  return { day, month, year };
}

const day = parseInt(prompt('Введите день:'));
const month = parseInt(prompt('Введите месяц:'));
const year_ = parseInt(prompt('Введите год:'));

// Вывод следующей даты
const nextDate = getNextDate(day, month, year_);
console.log(`Следующая дата: ${nextDate.day}.${nextDate.month}.${nextDate.year}`);
