//JS for crossing out items
$("ul").on("click", "li", function(e){
  $(this).toggleClass("finished");
  e.stopPropagation();
})
//JS for deleting item with fade animation
$("ul").on("click", "span", function(e) {
  $(this).parent().addClass("finished");
  $(this).parent().fadeOut(500, function() {
    $(this).remove();
  });
  e.stopPropagation();
});
//JS for input box toggle
$("#image").on("click", function(e) {
  $("#input").fadeToggle();
  e.stopPropagation();
});
//JS for handling input passed to todo list
$("input[type='text']").on("keypress",function(e) {
  if (e.keyCode === 13){
    let newItem = $("input").val();
    $("input").val("");
    $("ul").append("<li><span class=\"hidden\"><i class=\"fas fa-trash-alt\"></i></span> " + newItem + " </li>");
  }
});
