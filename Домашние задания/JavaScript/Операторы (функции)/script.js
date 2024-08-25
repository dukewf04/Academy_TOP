// 1. Сравнение двух чисел
function compareNumbers(num1, num2) {
  if (num1 < num2) {
    return -1;
  } else if (num1 > num2) {
    return 1;
  } else {
    return 0;
  }
}

// 2. Факториал числа
function factorial(num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

// 3. Объединение цифр в число
function combineDigits(digit1, digit2, digit3) {
  return parseInt(digit1.toString() + digit2.toString() + digit3.toString());
}

// 4. Площадь прямоугольника или квадрата
function calculateArea(length, width) {
  if (width === undefined) {
    return length * length;
  } else {
    return length * width;
  }
}

// 5. Проверка совершенного числа
function isPerfectNumber(num) {
  let sumOfDivisors = 1;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      sumOfDivisors += i;
      if (i !== num / i) {
        sumOfDivisors += num / i;
      }
    }
  }
  return sumOfDivisors === num;
}

// 6. Совершенные числа в диапазоне
function isPerfect(num) {
  if (num === 1) {
    return false;
  }

  let sum = 1;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      sum += i;
      if (i !== Math.sqrt(num)) {
        sum += num / i;
      }
    }
  }
  return sum === num;
}

function perfectNumbersInRange(min, max) {
  console.log('Совершенные числа в диапазоне от', min, 'до', max, ':');
  for (let i = min; i <= max; i++) {
    if (isPerfect(i)) {
      console.log(i);
    }
  }
}

// 7. Форматирование времени
function formatTime(hours, minutes = 0, seconds = 0) {
  // Форматирование с нулями
  const formattedHours = hours.toString().padStart(2, '0');
  const formattedMinutes = minutes.toString().padStart(2, '0');
  const formattedSeconds = seconds.toString().padStart(2, '0');
  return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}

// 8. Преобразование времени в секунды
function timeToSeconds(hours, minutes, seconds) {
  return hours * 3600 + minutes * 60 + seconds;
}

// 9. Преобразование секунд в время
function secondsToTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const remainingSeconds = seconds % 60;
  return formatTime(hours, minutes, remainingSeconds);
}

// 10. Разница между датами
function dateDifference(hours1, minutes1, seconds1, hours2, minutes2, seconds2) {
  const date1Seconds = timeToSeconds(hours1, minutes1, seconds1);
  const date2Seconds = timeToSeconds(hours2, minutes2, seconds2);

  const differenceSeconds = Math.abs(date1Seconds - date2Seconds);

  return secondsToTime(differenceSeconds);
}
