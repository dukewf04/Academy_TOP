const orderForm = document.getElementById('orderForm');
const orderConfirmation = document.getElementById('orderConfirmation');

orderForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const book = document.getElementById('book').value;
  const quantity = document.getElementById('quantity').value;
  const name = document.getElementById('name').value;
  const deliveryDate = document.getElementById('deliveryDate').value;
  const address = document.getElementById('address').value;
  const comment = document.getElementById('comment').value;

  orderConfirmation.innerHTML = `
    ${name}, спасибо за заказ! 
    ${quantity} ${book} будет доставлен ${deliveryDate} по адресу ${address}.
    ${
      comment
        ? `
    Комментарий: ${comment}`
        : ''
    }
    `;
});
