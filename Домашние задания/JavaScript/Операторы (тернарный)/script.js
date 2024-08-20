//Задания, в которых необходимо использовать IF.
// 1. Определение знака числа
let number = prompt("Введите число:");

if (number > 0) {
  console.log("Число положительное");
} else if (number < 0) {
  console.log("Число отрицательное");
} else {
  console.log("Число равно нулю");
}

// 2. Проверка возраста
let age = prompt("Введите ваш возраст:");

if (age >= 0 && age <= 120) {
  console.log("Введенный возраст корректен");
} else {
  console.log("Введенный возраст некорректен");
}

// 3. Вывод модуля числа
let number2 = prompt("Введите число:");

if (number2 >= 0) {
  console.log(`Модуль числа ${number2} равен ${number2}`);
} else {
  console.log(`Модуль числа ${number2} равен ${-number2}`);
}

// 4. Проверка времени
let hours = prompt("Введите часы:");
let minutes = prompt("Введите минуты:");
let seconds = prompt("Введите секунды:");

if (hours >= 0 && hours <= 23 && minutes >= 0 && minutes <= 59 && seconds >= 0 && seconds <= 59) {
  console.log("Введенное время корректное");
} else {
  console.log("Введенное время некорректное");
}

// 5. Определение четверти
let x = prompt("Введите координату x:");
let y = prompt("Введите координату y:");

if (x > 0 && y > 0) {
  console.log("Точка находится в первой четверти");
} else if (x < 0 && y > 0) {
  console.log("Точка находится во второй четверти");
} else if (x < 0 && y < 0) {
  console.log("Точка находится в третьей четверти");
} else if (x > 0 && y < 0) {
  console.log("Точка находится в четвертой четверти");
} else if (x === 0 && y === 0) {
  console.log("Точка находится в начале координат");
} else if (x === 0) {
  console.log("Точка находится на оси Y");
} else {
  console.log("Точка находится на оси X");
}


//Задания, в которых необходимо использовать IF.
// Задание 1: Вывод названия месяца по номеру
const monthNumber = parseInt(prompt("Введите номер месяца (от 1 до 12):"));

let monthName;

switch (monthNumber) {
  case 1:
    monthName = "Январь";
    break;
  case 2:
    monthName = "Февраль";
    break;
  case 3:
    monthName = "Март";
    break;
  case 4:
    monthName = "Апрель";
    break;
  case 5:
    monthName = "Май";
    break;
  case 6:
    monthName = "Июнь";
    break;
  case 7:
    monthName = "Июль";
    break;
  case 8:
    monthName = "Август";
    break;
  case 9:
    monthName = "Сентябрь";
    break;
  case 10:
    monthName = "Октябрь";
    break;
  case 11:
    monthName = "Ноябрь";
    break;
  case 12:
    monthName = "Декабрь";
    break;
  default:
    monthName = "Неверный номер месяца";
}

console.log(monthName);

// Задание 2: Калькулятор
const num1 = parseFloat(prompt("Введите первое число:"));
const operator = prompt("Введите оператор (+ - * /):");
const num2 = parseFloat(prompt("Введите второе число:"));

let result;

switch (operator) {
  case "+":
    result = num1 + num2;
    break;
  case "-":
    result = num1 - num2;
    break;
  case "":
    result = num1 * num2;
    break;
  case "/":
    if (num2 === 0) {
      result = "Деление на ноль невозможно";
    } else {
      result = num1 / num2;
    }
    break;
  default:
    result = "Неверный оператор";
}

console.log(result);


//Задания, в которых необходимо использовать тернарный оператор.
// Запросить 2 числа и вывести большее из них.
let num1 = prompt("Введите первое число:");
let num2 = prompt("Введите второе число:");

let biggerNum = (num1 > num2) ? num1 : num2;
console.log("Больше число:", biggerNum);


// Запросить 1 число и проверить, оно кратно 5 или нет.
let num = prompt("Введите число:");

let isMultipleOfFive = (num % 5 === 0) ? "Число кратно 5" : "Число не кратно 5";
console.log(isMultipleOfFive);


//3. Запросить у пользователя название планеты. Если пользователь ввел «Земля» или «земля», то вывести «Привет, землянин!», в остальных случаях вывести «Привет, инопланетянин!».
let planet = prompt("Введите название планеты:");

let greeting = (planet.toLowerCase() === "земля") ? "Привет, землянин!" : "Привет, инопланетянин!";
console.log(greeting);