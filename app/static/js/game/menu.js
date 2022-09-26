
let menu = document.querySelector("#menu");
let navbar = document.querySelector(".navbar-left");

menu.addEventListener("click", function () {
    navbar.classList.toggle("active");
});