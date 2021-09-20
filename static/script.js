function showHide(event) {
  event.preventDefault();
  var div = document.getElementById("loading-icon");
  if (div.style.display == "none") {
    div.style.display = "";
  } else {
    div.style.display = "none";
  }
}

var form = document.getElementById("myForm");
form.addEventListener("submit", showHide);
