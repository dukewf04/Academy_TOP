let div = document.createElement("div");
div.className = "alert";
div.innerHTML = 'Привет <strong>Вася</strong>. Как сам.'
document.body.append(div);

li2.style.backgroundColor = 'red';
li2.before('before');

const liFirst = document.createElement('li');
liFirst.innerHTML = 'FirstLi'
ul3.prepend(liFirst);

const liLast = document.createElement('li');
liLast.innerHTML = 'LastLi'
ul3.append(liLast);