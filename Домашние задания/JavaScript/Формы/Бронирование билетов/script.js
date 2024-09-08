const direction = {
  pm: [1, 2, 3, 4, 10, 15, 20, 21, 23, 29, 30, 40, 50, 60, 70, 80, 90, 100],
  pd: [2, 6, 9, 12],
  sk: [15, 16, 17, 18, 20, 31, 40, 45],
};

const dir = document.getElementById('direction');
const orderConfirmation = document.getElementById('orderConfirmation');

search.onclick = () => {
  let seats = '';
  direction[dir.value].forEach((el) => {
    seats += `
      <div class="seats">
        <input type="checkbox" value="${el}" id="ch-${el}">
        <label for="ch-${el}">${el}</label>
      </div>
    `;
  });
  orderConfirmation.innerHTML = seats;
  book.style.display = 'block';
};

book.onclick = () => {
  let checkedSeats = document.querySelectorAll('input[type=checkbox]:checked');
  checkedSeats = Array.from(checkedSeats).map((item) => item.value);
  checkedSeats.forEach((item) => {
    tableSeats.innerHTML += `
      <tr>
        <td>${dir.options[dir.selectedIndex].innerText}</td>
        <td>${date.value}</td>
        <td>${item}</td>
      </tr>
    `;
  });

  tableSeats.style.display = 'block';
};
