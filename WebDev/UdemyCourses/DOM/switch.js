var button2 = document.querySelectorAll("button")[1];
var body = document.querySelector("body");
var text = document.querySelector("p");

button2.addEventListener("click", function() {
  body.classList.toggle("black");
  text.classList.toggle("text");
});