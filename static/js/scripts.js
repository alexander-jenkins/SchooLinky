// home button code
var homeButton = document.getElementById("homeBtn");
homeButton.onclick = function() {
    window.open("/", name="_self");
}

// code for the modal setName menu
var nameModal = document.getElementById("setName");
var nameBtn = document.getElementById("setNameBtn");
var nameSpan = document.getElementsByClassName("close")[0];
nameBtn.onclick = function() {
  nameModal.style.display = "block";
}
nameSpan.onclick = function() {
  nameModal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == nameModal) {
    nameModal.style.display = "none";
  }
}

// code for the modal addClass menu
var modal = document.getElementById("newClass");
var btn = document.getElementById("newClassBtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
  modal.style.display = "block";
}
span.onclick = function() {
  modal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}