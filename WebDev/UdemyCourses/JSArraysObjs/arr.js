movies = [
  {
    title: "Logan",
    rating: 9,
    haveSeen: true
  },
  {
    title: "Frozen 2",
    rating: 6.5,
    haveSeen: false
  },
  {
    title: "Casino Royale",
    rating: 8,
    haveSeen: true
  },
  {
    title: "Jumanji Remake",
    rating: 8.5,
    haveSeen: false
  }
]

movies.forEach(function(movie) {
  var notSeen = "have not";
  if (movie.haveSeen){
    var notSeen = "have";
  } 
  console.log(`I ${notSeen} seen ${movie.title}, it got ${movie.rating} out of 10 stars!`);
})