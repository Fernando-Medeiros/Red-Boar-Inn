
for (let i = 0; i < 15; i++) {

    let button = document.querySelector("#version-update-".concat(i))

    button.addEventListener("click", function () {
        button.classList.toggle("remove-display-none");
    })
}