let button_menu = document.querySelector("#menu");
let navbar = document.querySelector("#navbar");
let navbar_mobile = document.querySelector("#nav-mobile");


function showMenu() {

    button_menu.addEventListener("click", function () {
        navbar_mobile.classList.toggle("active-menu-mobile");
    });


    window.onscroll = () => {
        navbar_mobile.classList.remove("active-menu-mobile")
    };
};



function activateMobileMenu() {

    // When resizing the screen

    window.onresize = () => {

        if (window.innerWidth <= 800) {

            if (!button_menu.classList.value.includes('active')) {

                button_menu.classList.toggle("active");
                navbar.classList.toggle("disabled-navbar-a");
            }

        } else {
            button_menu.classList.remove("active");
            navbar.classList.remove("disabled-navbar-a");
            navbar_mobile.classList.remove("active-menu-mobile")
        }
    };


    // when refreshing the page

    if (window.innerWidth <= 800) {

        if (!button_menu.classList.value.includes('active')) {

            button_menu.classList.toggle("active");
            navbar.classList.toggle("disabled-navbar-a");
            navbar_mobile.classList.remove("active-menu-mobile")
        }
    }
}


showMenu()
activateMobileMenu()