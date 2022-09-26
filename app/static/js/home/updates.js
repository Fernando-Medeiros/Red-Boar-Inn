
let navbar = document.querySelector(".container-updates-main");

for (let i = 0; i <= 10; i++) {

    let menu = document.querySelector("#version-update-".concat(i))

    menu.addEventListener("click", function () {
        menu.classList.toggle("remove-display-none");
    })
}