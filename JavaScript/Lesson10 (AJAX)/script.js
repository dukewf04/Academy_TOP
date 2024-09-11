//Ajax — технология для взаимодействия с сервером без перезагрузки страницы.

let request;
// Реализация проверки на создание xml запросов
if (window.XMLHttpRequest) {
  request = new XMLHttpRequest();
  // Кросбраузерное решение на создание запроса
} else {
  request = new ActiveXObject("Microsoft.XMLHTTP");
}

// request.open("GET", "text.txt");

// request.onreadystatechange = function () {
//   console.log("readyState = " + request.readyState);
//   if (request.readyState == 4) {
//     alert(request.response.firstName);
//   }
// };
// request.send();

// statusText / status - состояние завершения запроса
// responseType - указывает, ответ какого типа нам пришел от сервера
// ("", text, array, document, json, blob)

// ------------ События onload, onloadend, onerror ---------------
// onload - вызывается только тогда, когда все данные будут загружены
// onerror — вызывается, когда запрос завершился некорректно
// onprogress  — периодически вызывается во время загрузки ответа

// request.onloadend = function (event) {
//   if (request.status === 200) {
//     alert(`Загружено: ${event.loaded}`);
//   }
// };

// request.onload = function (event) {
//   if (request.status === 404) {
//     alert(request.response);
//   }
// };

// request.onerror = function () {
//   alert("Ошибка");
// };

// request.send();


// ----------------- Запросы на удаленный сервер -----------------------

request.open("GET", "https://jsonplaceholder.typicode.com/posts/2");

request.onloadend = function (event) {
  if (request.status === 200) {
    alert(request.response);
  }
};

request.onerror = function () {
  alert("Ошибка");
};
request.send();
