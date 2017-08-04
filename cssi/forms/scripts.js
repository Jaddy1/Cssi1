function greeting(){
  var userName = $('#username').val();
  alert("Hi" + " " + userName + ", you have beautiful eyes");
  var header = $("h2");
  header.text(userName + ", Welcome!");
}

function setup(){
  $("#ok_button").click(greeting);
}

$(document).ready(setup);
