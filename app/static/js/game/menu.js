let button_menu = document.querySelector("#menu");
let navbar = document.querySelector(".navbar-left");


function showMenu() {

    button_menu.addEventListener("click", function () {
        navbar.classList.toggle("enable-icons")
        navbar.classList.toggle("active")
    })

    window.onscroll = () => {
        navbar.classList.remove("enable-icons")
        navbar.classList.remove("active")
    }
}


function activateMobileMenu() {

    // When resizing the screen

    window.onresize = () => {

        if (window.innerWidth <= 800) {

            if (!navbar.classList.value.includes('disabled-icons')) {
                navbar.classList.toggle("disabled-icons")
            }
        } else {
            navbar.classList.remove("disabled-icons")
        }
    };

    // when refreshing the page

    if (window.innerWidth <= 800) {

        if (!navbar.classList.value.includes('disabled-icons')) {
            navbar.classList.toggle("disabled-icons")
        }
    }
}


showMenu()
activateMobileMenu()