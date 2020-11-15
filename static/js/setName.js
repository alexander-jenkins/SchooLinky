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