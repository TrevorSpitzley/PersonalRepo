let ans = 8
let guess = prompt("Think of a number 1-10, inclusively. Submit your guess.");
if (Number(guess) === ans) {
  alert("Great job! You guessed correctly!");
}
else if (Number(guess) > ans) {
  alert("You are too high, refresh again and guess lower.");
}
else if (Number(guess) < ans) {
  alert("You are too low, refresh again and guess higher.");
}
