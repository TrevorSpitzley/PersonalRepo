var age = prompt("How many years old are you?");
// var inDays = userYears * 365.25;
// alert("You have been alive for approximately " + inDays + " days! Congrats!");
if (age < 0){
  alert("Cannot pass a negative age. Refresh and try again");
}
if (age == 21){
  console.log("Happy birthday!");
}
if (age % 2 !== 0) {
  console.log("Your age is odd.");
}
if (age % Math.sqrt(age) === 0) {
  console.log("You are a perfect square!");
}
