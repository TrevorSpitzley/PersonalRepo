let btn = document.querySelector("button");
let num = document.getElementById("counter");
let count = 0;

num.textContent = count;
btn.addEventListener("click", function () {
  count++;
  num.textContent = count;
});
