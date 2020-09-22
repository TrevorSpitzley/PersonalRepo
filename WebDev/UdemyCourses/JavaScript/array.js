//Print list in reverse
function printReverse(list) {
  if (list.length > 0) {
    for (var i = list.length - 1; i >= 0; i--) {
      console.log(list[i]);
    }
  }
}
//Check if list is uniform
function isUniform(list) {
  if (list.length > 0) {
    var first = list[0];
    var ans = true;
    list.splice(1).forEach(function(word) {
      if (first !== word){
        ans = false;
      } 
    });
    return ans;
  }
  return false;
}
//Sum up array
function sumArray(list) {
  var ans = 0;
  if (list.length > 0){
    if ( typeof list[0] === "number") {
      list.forEach(function(currNum) {
        ans += currNum;
      }
    )}
    return ans;
  }
  return -1;
}
//Max of array
function maxArray(list) {
  if (list.length > 0) {
    var max = list[0];
    for (var i = 0; i < list.length; i++) {
      if (list[i] > max){
        var max = list[i];
      }  
    }
    return max;
  }
  return -1;
}