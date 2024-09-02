const getStructure = () => {
  var c = document.documentElement.childNodes;
  var msg = "";

  for (var i = 0; i < c.length; i++) {
    let d = c[i];
    msg += i + 1 + "." + d.tagName + "(" + d.nodeName + ")<br>";

    if (d.hasChildNodes()) {
        let e = d.childNodes
        for(var j = 0; j < c.length; j++) {
            let f = e[j];
            msg += `&nbsp;&nbsp;${j+1}.${f.tagName}(${f.nodeName})<br>`
        }
    }
  }

  window.d2.innerHTML = msg;
};

document.onmousemove = function(e) {
    console.log(e.pageX)
}