function showNews() {
    let button_news = document.querySelector("#button-news")
    let news = document.querySelector("#news")

    button_news.addEventListener("click", function () {
        news.classList.toggle('hidden')
    })
}


function showRankLevel() {
    let button_rank = document.querySelector("#button-by-level")
    let info = document.querySelector("#info-by-level")

    button_rank.addEventListener("click", function () {
        info.classList.toggle('hidden')
    })
}


function showRankVictory() {
    let button_rank = document.querySelector("#button-by-victory")
    let info = document.querySelector("#info-by-victory")

    button_rank.addEventListener("click", function () {
        info.classList.toggle('hidden')
    })
}


function attack() {
    let attack = document.querySelector("#attack")
    let health = document.querySelector("#opponent_health")
    let current_health = document.querySelector("#opponent_current_health")

    // SET C_HP / T_HP
    health.replaceChildren((current_health.getAttribute('value') + ' / ' + health.getAttribute('value')))

    attack.addEventListener("click", function () {

        // DAMAGE
        current_health.setAttribute('value', current_health.getAttribute('value') - 5)

        var max_size = health.scrollWidth
        var current_size = health.getAttribute('value') / max_size

        // UPDATE HEALTH BAR
        current_health.setAttribute('style', 'width:'.concat(current_health.getAttribute('value') / current_size) + 'px')

        // SET NEW C_HP / T_HP
        health.replaceChildren((current_health.getAttribute('value') + ' / ' + health.getAttribute('value')))
    })
}

function flee() {
    let flee = document.querySelector("#flee")

    flee.addEventListener("click", function () {
    })

}

showNews()
showRankLevel()
showRankVictory()

flee()
attack()