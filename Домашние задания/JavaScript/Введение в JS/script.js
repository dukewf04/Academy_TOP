// 1. Запросите у пользователя его имя и выведите в ответ: «Привет, его имя!».
// const name = prompt('Как тебя зовут');
// alert(`Привет, ${name}!`);

// 2. Запросите у пользователя год его рождения, посчитайте, сколько ему лет и выведите результат.
// Текущий год укажите в коде как константу.
// const currentYear = 2024;
// const year = prompt('Какого ты года рождения');
// alert(`Тебе ${Number(currentYear - year)} лет.`);

// 3. Запросите у пользователя длину стороны квадрата и выведите периметр такого квадрата.
// const length = prompt('Введите длину квадрата');
// alert(`Периметр квадрата ${4*Number(length)}`);

// 4. Запросите у пользователя радиус окружности и выведите площадь такой окружности.
// const r = prompt('Введите радиус окружности');
// alert(`Площадь окружности ${3.14 * Number(r) ** 2}`);

/*
  5. Запросите у пользователя расстояние в км между двумя городами и за сколько часов он хочет добраться.
  Посчитайте скорость, с которой необходимо двигаться, чтобы успеть вовремя.
*/
// const lengthBetweenCities = prompt("Введите расстояние между 2 городами в км")
// const wishTime = prompt("За сколько часов хотите добраться")
// alert(`Вы должны двигаться со скоростью ${Number(lengthBetweenCities/wishTime)} км/ч`)

/*
  6. Реализуйте конвертор валют. Пользователь вводит доллары, программа переводит в евро.
  Курс валюты храните в константе.
*/
// const dollarEuroRate = 0.92;
// const dollars = prompt('Введите количество долларов');
// alert(`${dollars} долларов будет ${dollarEuroRate * Number(dollars)} евро`);

/*
  7. Пользователь указывает объем флешки в Гб.
  Программа должна посчитать сколько файлов размером в 820 Мб помещается на флешку.
*/
// const volume = prompt('Введите объем флешки в Гб');
// const filesCount = Math.floor((volume * 1024) / 820);
// alert(`Файлов размером в 820 Мб вместится на флешку ${filesCount} штук`);

/*
  8. Пользователь вводит сумму денег в кошельке и цену одной шоколадки.
  Программа выводит сколько шоколадок может купить пользователь и сколько сдачи у него останется. 
*/
// const money = prompt('Введите сколько у вас денег в кошельке');
// const chocolateCost = prompt('Введите стоимость одной шоколадки (руб)');
// const chocolateCount = Math.floor((money) / chocolateCost);
// const change = money - chocolateCost * chocolateCount
// alert(`Вы сможете купить ${chocolateCount} шоколадок и останется сдачи ${change} рублей.`)

/*
  9. Запросите у пользователя трехзначное число и выведите его задом наперед.
  Для решения задачи вам понадобится оператор % (остаток от деления).
*/
// const number = prompt('Введите трехзначное число');
// const reversNumber = String(number % 10) + String(Math.floor(number / 10) % 10) + String(Math.floor(number / 100));
// alert(`Число задом наперед ${reversNumber}`);

/*
  10. Запросите у пользователя целое число и выведите в ответ, четное число или нет.
  В задании используйте логические операторы. В задании не надо использовать if или switch.
*/
// const number = prompt('Введите целое число');
// const evenOrOdd = ['нечетное', 'четное'];
// alert(`Число ${number} ${evenOrOdd[Number(number % 2 === 0)]}`);
// console.log(Number(number % 2 === 0), number % 2 === 0)
