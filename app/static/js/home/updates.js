
for (let i = 0; i < 15; i++) {

    let button = document.querySelector("#version".concat(i));
    let updates = document.querySelector("#p_update".concat(i));

    button.addEventListener("click", function () {

        if (updates.classList.contains("hidden")) {
            updates.classList.remove("hidden")
        }
        else {
            updates.classList.add("hidden")
        }
    })
}