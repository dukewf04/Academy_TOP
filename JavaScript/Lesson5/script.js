// Задание 1
// const getMinNumber = (a, b) => {
//   return Math.min(a, b);
// };
// console.log(getMinNumber(20, 3));

// Задание 2
// const stepen = (a, b) => {
//   return a ** b;
// };
// console.log(stepen(3, 3));

// Задание 3
// const calculate = (a, b, znak) => {
//   let result;
//   switch (znak) {
//     case "+":
//       result = Number(a) + Number(b);
//       break;
//     case "-":
//       result = Number(a) - Number(b);
//       break;
//     case "*":
//       result = Number(a) * Number(b);
//       break;
//     case "/":
//       result = Number(a) / Number(b);
//       break;
//   }
//   return result;
// };
// console.log(calculate(3, 3, "+"));

// Задание 4
// const isNumberPrime = (val) => {
//   let count = 0;
//   for (let i = 2; i <= Number(val) / 2; i++) {
//     if (Number(val) % i === 0) {
//       return `Число ${val} не простое`;
//     }
//   }

//   return `Число ${val} простое`;
// };
// console.log(isNumberPrime(11));

// Задание 7
// var value_number = +prompt("Сколько чисел будем суммировать?");
// const summNumbers = (value_number) => {
//   let summ = 0;
//   for (let i = 0; i < value_number; i++) {
//     let value_user = +prompt("Введите число");
//     summ += value_user;
//   }
//   return summ;
// };
// console.log(summNumbers(value_number));

// Задание 8
// const maxNumber = (arr) => {
//   return Math.max(...arr);
// };
// const arr = [0, 500, 10, 22, 4];
// console.log(`Максимальное из чисел ${arr}: ${maxNumber(arr)}`);

// Задание 9
// const evenOddNumbers = (numbers, isEven) => {
//   console.log(
//     numbers.filter((item) => (isEven ? item % 2 === 0 : item % 2 !== 0))
//   );
// };
// const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// evenOddNumbers(arr, false);

// Задание 10
// const isLeap = (year) => {
//   if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
//     return 29;
//   } else {
//     return 28;
//   }
// };

// const nextDate = (day, month, year) => {
//   // prettier-ignore
//   const daysInMonth = [31, isLeap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

//   let newDay = day + 1;
//   let newMonth = month;
//   let newYear = year;

//   if (day === daysInMonth[month - 1]) {
//     newDay = 1;
//     if (month < 12) {
//       newMonth += 1;
//     } else {
//       newMonth = 1;
//       newYear += 1;
//     }
//   }

//   return `${newDay}.${newMonth}.${newYear}`;
// };
// console.log(nextDate(31, 12, 2024));
