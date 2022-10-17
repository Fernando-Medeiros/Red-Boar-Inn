let man = document.querySelector("#man");
let woman = document.querySelector("#woman");
let sprite = document.querySelector("#sprite");


function showSprite() {

    man.addEventListener("click", function () {
        if (man.checked) {

            sprite.src = "/static/img/sprites/man/peasant.png"
            woman.checked = ''
        }
    })

    woman.addEventListener("click", function () {
        if (woman.checked) {

            sprite.src = "/static/img/sprites/woman/peasant.png"
            man.checked = ''
        }
    })
}

showSprite()