var screen = document.getElementById('popupScreen');
// button
var btn = document.getElementById('signup');
// get the close icon
var close = document.getElementsByClassName('close')[0];

// when the user clicks the button open popup
btn.onclick = function() {
	screen.style.display = "block";
}

close.onclick = function() {
  screen.style.display = "none";
}