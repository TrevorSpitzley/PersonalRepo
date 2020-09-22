//Function to return true if passed int is even
function isEven(int) {
  return int % 2 === 0;
}
//Function to return the factorial of a number
function factorial(int) {
  var ans = 1;
  while (int !== 0) {
    ans *= int;
    int--;
  }
  return ans;
}
//Function to turn a string with hyphens to underscores
function kebabToSnake(string) {
  // var ans = "";
  // for (var i = 0; i < string.length; i++) {
  //   if (string[i] !== "-") {
  //     ans += string[i];
  //   } else {
  //     ans += "_";
  //   }
  // }
  // return ans;
  return string.replace(/-/g, "_");
}