const firstnameInput = document.getElementById('firstname');
const lastnameInput = document.getElementById('lastname');
const birthdayInput = document.getElementById('birthday');
const maleRadio = document.getElementById('male');
const femaleRadio = document.getElementById('female');
const countryInput = document.getElementById('country');
const cityInput = document.getElementById('city');
const htmlCheckbox = document.getElementById('html');
const cssCheckbox = document.getElementById('css');
const jsCheckbox = document.getElementById('js');
const saveButton = document.querySelector('button');

const outputContainer = document.createElement('div');
outputContainer.classList.add('output');
document.body.appendChild(outputContainer);

saveButton.addEventListener('click', () => {
  const firstName = firstnameInput.value;
  const lastName = lastnameInput.value;
  const birthday = birthdayInput.value;
  const gender = maleRadio.checked ? 'Male' : femaleRadio.checked ? 'Female' : 'Not specified';
  const country = countryInput.value;
  const city = cityInput.value;
  const skills = [];
  if (htmlCheckbox.checked) skills.push('HTML');
  if (cssCheckbox.checked) skills.push('CSS');
  if (jsCheckbox.checked) skills.push('JS');

  outputContainer.innerHTML = `
    <h2>Result</h2>
    <p><strong>First name:</strong> ${firstName}</p>
    <p><strong>Last name:</strong> ${lastName}</p>
    <p><strong>Birthday:</strong> ${birthday}</p>
    <p><strong>Gender:</strong> ${gender}</p>
    <p><strong>Country:</strong> ${country}</p>
    <p><strong>City:</strong> ${city}</p>
    <p><strong>Skills:</strong> ${skills.join(', ')}</p>
  `;
});
