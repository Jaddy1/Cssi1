function setup() {
  $("body").append("<div></div");
  $("div").mouseenter(changeColorToBlue);
  $("di").mouseleave(changeColorToRed);

}

function changeColorToRed(){
  $(this).removeClass("blue")
  $(this).addClass("red");
}

function changeColorToBlue(){
  $(this).removeClass("red")
  $(this).addClass("blue");
}
function greeting(){
  var name = $("#nameInput")
  var header = $("h2")
  header.text("Hi " + name + ", welcome to the site. Feel free to play around with the box thing");
}

$(document).ready(setup);
