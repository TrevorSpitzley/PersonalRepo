let i = -1;
setInterval(function() {
  const pics = ["pfp.png", "Checker_Piece_Red.png"];
  let pic = document.getElementsByTagName("img")[0];
  i++;
  let photo = pics[i % 2];
  // pic.setAttribute("src", photo);
  pic.srcset = photo;
  // console.log(i);
}, 1000);