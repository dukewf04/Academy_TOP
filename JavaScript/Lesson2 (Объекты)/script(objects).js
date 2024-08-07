// Работа с объектами
// const obj = new Object();
// const arr = new Array();
// var obj2 = {};
// obj.name = 'Vasya';
// obj.age = '21';
// obj.address = {
//     street: 'Zarechnaya',
//     home: 10
// }

// for (let tempProperty in obj) {
//     console.log(tempProperty)
//     console.log(obj[tempProperty])
// }

// Массивы
const arr = new Array();
arr.push(0, 1, 5, 'hello', '')
arr[10] = 100

for(var i=0; i<arr.length; i = i + 5) {
    console.log(arr[i])
}