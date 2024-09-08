// Правильные ответы
const correctAnswers = [5, 5];

const getCookies = () => {
  let x = document.cookie;
  let s = x.split('; ');
  let cookieObject = {};
  var c;
  for (let i = 0; i < s.length; i++) {
    c = s[i].split('=');
    cookieObject[c[0]] = c[1];
  }

  return cookieObject;
};

const onLoad = () => {
  const cookieObject = getCookies();

  if ('superTest' in cookieObject) {
    if ('q2' in JSON.parse(cookieObject['superTest'])) {
      let correctAnswerCount = 0;
      Object.values(JSON.parse(cookieObject['superTest'])).forEach((item, i) => {
        if (Number(item) === correctAnswers[i]) correctAnswerCount++;
      });

      result.innerHTML = `Result: ${correctAnswerCount} correct answers to 2 questions`;
      result.style.display = 'block';
      document.cookie = `superTest=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    } else if ('q1' in JSON.parse(cookieObject['superTest'])) {
      question2.style.display = 'block';
    }
  } else {
    question1.style.display = 'block';
  }
};

next.onclick = () => {
  const a1 = document.querySelector('input[name="q1"]:checked').value;
  const obj = {
    q1: a1,
  };
  document.cookie = `superTest=${JSON.stringify(obj)};path=/`;
};

finish.onclick = () => {
  const cookieObject = getCookies();
  const a2 = document.querySelector('input[name="q2"]:checked').value;
  const obj = {
    q2: a2,
  };

  document.cookie = `superTest=${JSON.stringify({
    ...JSON.parse(cookieObject['superTest']),
    ...obj,
  })};path=/`;
};
