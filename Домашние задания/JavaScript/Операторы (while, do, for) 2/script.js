// Задания, в которых необходимо использовать WHILE.
// 1. Вывести # столько раз, сколько указал пользователь.
// let num1 = parseInt(prompt("Введите количество символов #"));
// let count1 = 0;
// while (count1 < num1) {
//   console.log("#");
//   count1++;
// }

// 2. Пользователь ввел число, а на экран вывелись все числа от введенного до 0.
// let num2 = parseInt(prompt("Введите число:"));
// while (num2 >= 0) {
//   console.log(num2);
//   num2--;
// }

// 3. Запросить число и степень. Возвести число в указанную степень и вывести результат.
// let num3 = parseInt(prompt("Введите число:"));
// let power = parseInt(prompt("Введите степень:"));
// let result = num3;
// let count3 = 0;
// while (count3 < power) {
//   result *= num3;
//   count3++;
// }
// console.log(num3 + " в степени " + power + " равно " + result);

// 4. Запросить 2 числа и найти все общие делители.
// let num4_1 = parseInt(prompt("Введите первое число:"));
// let num4_2 = parseInt(prompt("Введите второе число:"));
// let i = 1;
// console.log("Общие делители чисел " + num4_1 + " и " + num4_2 + ":");
// while (i <= Math.min(num4_1, num4_2)) {
//   if (num4_1 % i === 0 && num4_2 % i === 0) {
//     console.log(i);
//   }
//   i++;
// }

// 5. Посчитать факториал введенного пользователем числа.
// let num5 = parseInt(prompt("Введите число для расчета факториала:"));
// let factorial = 1;
// let count5 = 1;
// while (count5 <= num5) {
//   factorial = factorial * count5;
//   count5++;
// }
// console.log("Факториал " + num5 + " равен " + factorial);

// Задания, в которых необходимо использовать DO WHILE.
//1. Решение примера 2 + 2 * 2
// let answer;
// do {
//   answer = prompt("Решите пример 2 + 2 * 2:");
//   if (answer != 6) {
//     alert("Неверно! Попробуйте снова.");
//   }
// } while (answer != 6);

// alert("Правильно! Ответ - 6");

// 2. Деление числа 1000 на 2
// let number = 1000;
// let count = 0;

// do {
//   number /= 2;
//   count++;
// } while (number >= 50);

// console.log(`Число: ${number}`);
// console.log(`Количество делений: ${count}`);

// Задания, в которых необходимо использовать FOR.
// 1. Вывести все числа от 1 до 100, которые кратные указанному пользователем числу.
// const multiple = parseInt(prompt("Введите число для кратности: "));

// for (let i = 1; i <= 100; i++) {
//   if (i % multiple === 0) {
//     console.log(i);
//   }
// }

// 2. Вывести каждый 4-й элемент из указанного пользователем диапазона.
// const min = parseInt(prompt("Введите минимальное значение диапазона: "));
// const max = parseInt(prompt("Введите максимальное значение диапазона: "));

// for (let i = min; i <= max; i += 4) {
//   console.log(i);
// }

// 3. Запросить число и проверить, простое ли оно.
// const number = parseInt(prompt("Введите число: "));
// let isPrime = true;
// if (number <= 1) {
//   isPrime = false;
// } else {
//   for (let i = 2; i <= Math.sqrt(number); i++) {
//     if (number % i === 0) {
//       isPrime = false;
//       break;
//     }
//   }
// }

// if (isPrime) {
//   console.log("Число простое.");
// } else {
//   console.log("Число не простое.");
// }