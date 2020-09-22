var score1 = document.getElementById("score1");
var score2 = document.getElementById("score2");
var limit = document.getElementById("limit");
var p1 = document.getElementById("player");
var p1Score = 0;
var p2 = document.getElementById("player2");
var p2Score = 0;
var reset = document.getElementById("reset");
var input = document.getElementById("input");
var game = true;
var rounds = 5;

input.addEventListener("click", function() {
  rounds = input.valueAsNumber;
  limit.textContent = rounds;
});

p1.addEventListener("click", function() {
  if (game) {
    p1Score++;
    score1.textContent = p1Score;
  }
  if (p1Score >= rounds){
    game = false;
    score1.style.backgroundColor = "green";
  } 
});

p2.addEventListener("click", function() {
  if (game) {
    p2Score++;
    score2.textContent = p2Score;
  }
  if (p2Score >= rounds){
    game = false;
    score2.style.backgroundColor = "green";
  } 
});

reset.addEventListener("click", function() {
  p1Score = 0;
  p2Score = 0;
  score1.textContent = p1Score;
  score2.textContent = p2Score;
  score1.style.backgroundColor = "white";
  score2.style.backgroundColor = "white";
  game = true;
});