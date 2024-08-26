const td = document.querySelectorAll("td, th");
tab.onmouseover = (e) => {
  td.forEach((item) => {
    item.style.backgroundColor = "bisque";
  });  
  e.target.style.backgroundColor = "red";
};
