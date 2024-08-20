// 1. Сумма чисел в диапазоне:
function sumOfRange() {
  let start = parseInt(prompt("Введите начальное число диапазона:"));
  let end = parseInt(prompt("Введите конечное число диапазона:"));
  let sum = 0;

  for (let i = start; i <= end; i++) {
    sum += i;
  }

  console.log(`Сумма чисел в диапазоне от ${start} до ${end}: ${sum}`);
}

sumOfRange();


// 2. Наибольший общий делитель:
function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

let num1 = parseInt(prompt("Введите первое число:"));
let num2 = parseInt(prompt("Введите второе число:"));
console.log(`Наибольший общий делитель чисел ${num1} и ${num2}: ${gcd(num1, num2)}`);


// 3. Делители числа:
function divisors(num) {
  let divisorsArray = [];

  for (let i = 1; i <= num; i++) {
    if (num % i === 0) {
      divisorsArray.push(i);
    }
  }

  console.log(`Делители числа ${num}: ${divisorsArray.join(', ')}`);
}

let number = parseInt(prompt("Введите число:"));
divisors(number);


// 4. Количество цифр в числе:
function countDigits(num) {
  let count = 0;

  while (num !== 0) {
    num = Math.floor(num / 10);
    count++;
  }

  console.log(`Количество цифр в числе: ${count}`);
}

let inputNumber = parseInt(prompt("Введите число:"));
countDigits(inputNumber);


// 5. Статистика 10 чисел:
function analyzeNumbers() {
  let positiveCount = 0;
  let negativeCount = 0;
  let zeroCount = 0;
  let evenCount = 0;
  let oddCount = 0;

  for (let i = 0; i < 10; i++) {
    let number = parseInt(prompt(`Введите число ${i + 1}:`));

    if (number > 0) {
      positiveCount++;
    } else if (number < 0) {
      negativeCount++;
    } else {
      zeroCount++;
    }

    if (number % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  console.log(`Статистика:`);
  console.log(`Положительных чисел: ${positiveCount}`);
  console.log(`Отрицательных чисел: ${negativeCount}`);
  console.log(`Нулей: ${zeroCount}`);
  console.log(`Четных чисел: ${evenCount}`);
  console.log(`Нечетных чисел: ${oddCount}`);
}

analyzeNumbers();

// 6. Зациклить калькулятор
let continueCalc = true;

while (continueCalc) {
  let num1 = parseFloat(prompt("Введите первое число:"));
  let num2 = parseFloat(prompt("Введите второе число:"));
  let operator = prompt("Введите знак операции (+, -, , /):");

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
      result = "Некорректный знак операции";
  }

  alert(`Результат: ${result}`);
  continueCalc = confirm("Хотите решить еще один пример?");
}


// 7. Сдвиг цифр числа
let number_ = parseInt(prompt("Введите число:"));
let shift = parseInt(prompt("Введите количество цифр для сдвига:"));

let digits = number_.toString().split('');
let shiftedDigits = digits.slice(shift).concat(digits.slice(0, shift));
let shiftedNumber = parseInt(shiftedDigits.join(''));

alert(`Результат: ${shiftedNumber}`);


// 8. Зациклить вывод дней недели
const daysOfWeek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"];
let dayIndex = 0;

do {
  alert(daysOfWeek[dayIndex]);
  dayIndex = (dayIndex + 1) % daysOfWeek.length;
} while (confirm("Хотите увидеть следующий день?"));



// 9. Таблица умножения
for (let i = 2; i <= 9; i++) {
  let row = "";
  for (let j = 1; j <= 10; j++) {
    row += `${i}  ${j} = ${i * j}\t`;
  }
  console.log(row);
}

// 10. Игра "Угадай число"
let min = 0;
let max = 100;

alert("Загадайте число от 0 до 100");

while (true) {
  let N = Math.floor((min + max) / 2);
  let answer = prompt(`Ваше число > ${N}, < ${N} или == ${N}?`);

  if (answer === ">") {
    min = N + 1;
  } else if (answer === "<") {
    max = N - 1;
  } else if (answer === "==") {
    alert(`Я угадал! Ваше число ${N}`);
    break;
  } else {
    alert("Неверный ввод. Введите >, < или ==");
  }
}