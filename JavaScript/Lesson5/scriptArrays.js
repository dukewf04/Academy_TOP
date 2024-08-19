// Задание 1
// const tooStr = (str1, str2) => {
//   const result =
//     str1.length === str2.length ? 0 : str1.length > str2.length ? 1 : -1;

//   console.log(result);
// };

// const str1 = prompt("Введите строку 1");
// const str2 = prompt("Введите строку 2");
// tooStr(str1, str2);

// Задание 2
// const upFirstLetter = (str) => {
//     return `${str[0].toUpperCase()}${str.slice(1)}`
// }
// console.log(upFirstLetter('привет мир'))

// Задание 3
// const getCountVowels = (str) => {
//   const vowelsArr = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"];
//   return str
//     .split("")
//     .filter((item) => vowelsArr.includes(item.toLocaleLowerCase())).length;
// };
// console.log(getCountVowels("прИвет"));

// Задание 4
// const checkSpam = (str) => {
//   const spamList = [
//     "100% бесплатно",
//     "увеличение продаж",
//     "только сегодня",
//     "не удаляйте",
//     "xxx",
//   ];

//   let isSpam = false;

//   spamList.forEach((item) => {
//     if (str.toLowerCase().indexOf(item) !== -1) {
//         isSpam = true;
//       return;
//     }
//   });

//   return isSpam;
// };
// console.log(checkSpam("Hello world xxx"));


// Задание 5
// const stringTransform = (str, len) => {
//     if (str.length > len) {
//         return `${String(str).slice(0, len - 3)}...`
//     }

//     return str;
// }

// console.log(stringTransform('Привет мир, как дела', 11))