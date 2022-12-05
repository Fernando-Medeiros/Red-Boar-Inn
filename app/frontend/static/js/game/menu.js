let button_menu = document.querySelector("#menu")
let navbar = document.querySelector("#navbar")
let navbar_mobile = document.querySelector("#navbar-left-mobile")
let navbar_default = document.querySelector("#navbar-left-default");

function showMenu() {

    button_menu.addEventListener("click", function () {
        navbar_default.classList.toggle("hidden")
        navbar.classList.toggle("hidden")
        navbar_mobile.classList.toggle("hidden")
    })
}

showMenu()