var button = document.querySelector("button");
var text = document.querySelector("p");

var clicks = 0;

button.addEventListener("click", function() {
  clicks++;
  if (clicks === 1){
    text.textContent = `I have been clicked ${clicks} time.`
  }
  else if (clicks > 1){
    text.textContent = `I have been clicked ${clicks} times.`
  }
});
