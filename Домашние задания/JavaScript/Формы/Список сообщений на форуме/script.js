send.addEventListener('click', () => {
  const name = document.getElementById('name');
  const message = document.getElementById('message');
  const dt = new Date();
  const currentDate = `${dt.getDate()}.${dt.getMonth()}.${dt.getFullYear()}`
  container.innerHTML += `
    <div id="posts" class="posts">
      <span style="margin-left: 10px;">${name.value}</span>
      <span style="margin-right: 10px;">${dt}</span>
      <div class="posts-message">${message.value}</div>
    </div><br/>
  `
})