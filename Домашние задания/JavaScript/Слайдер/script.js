// Задание 2. Галерея.
let arr = [
  "https://garden-zoo.ru/userfiles/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D0%BA%D0%BE%D1%82%D1%8B%20%D1%82%D0%B0%D0%BA%D0%B8%D0%B5%20%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%BE%D0%BC%D0%B5%D1%80%D0%BD%D1%8B%D0%B5.jpg",
  "https://cdnn21.img.ria.ru/images/07e4/0c/0a/1588643462_0:71:2753:1620_1920x0_80_0_0_268ae387f0eed00335c1d31cd1bc0fed.jpg",
  "https://opis-cdn.tinkoffjournal.ru/mercury/kitty-cat-cover-in.1hvzlnzda8kv..jpg",
];
let image = 1;
imageSlider.src = arr[image];
const backf = () => {
  if (image <= 0) {
    forward.style.backgroundColor = "white";
    back.style.backgroundColor = "red";
  } else {
    forward.style.backgroundColor = "white";
    image -= 1;
    imageSlider.src = arr[image];
  }
};

const forwardf = () => {
  console.log(image);
  if (image >= 2) {
    forward.style.backgroundColor = "red";
    back.style.backgroundColor = "white";
  } else {
    back.style.backgroundColor = "white";
    image += 1;
    imageSlider.src = arr[image];
  }
};
