var one = document.getElementById("first");
var two = document.getElementById("scd");
var three = document.getElementById("third");
var content = document.getElementById("content");

one.addEventListener("click", function() {
  content.innerHTML = "One";
});

two.addEventListener("click", function() {
   content.innerHTML = "Two";
});

three.addEventListener("click", function() {
   content.innerHTML = "Three";
});
