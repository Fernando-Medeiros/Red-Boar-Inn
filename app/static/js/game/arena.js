function showLogs() {
    let button_logs = document.querySelector("#button-logs")
    let logs = document.querySelector("#logs")

    button_logs.addEventListener("click", function () {
        logs.classList.toggle('active')
    })
}


function showRankLevel() {
    let button_rank = document.querySelector("#button-by-level")
    let info = document.querySelector("#info-by-level")

    button_rank.addEventListener("click", function () {
        info.classList.toggle('active')
    })
}


function showRankVictory() {
    let button_rank = document.querySelector("#button-by-victory")
    let info = document.querySelector("#info-by-victory")

    button_rank.addEventListener("click", function () {
        info.classList.toggle('active')
    })
}


function attack() {
    let attack = document.querySelector("#attack")
    let opponent_img = document.querySelector("#opponent")
    let health = document.querySelector("#health")
    let current_health = document.querySelector("#current_health")

    health.replaceChildren((current_health.getAttribute('value') + '/' + health.getAttribute('value')))

    attack.addEventListener("click", function () {
        var hit = current_health.setAttribute('value', current_health.getAttribute('value') - 5)

        var max_size = 112
        var current_size = health.getAttribute('value') / max_size

        health.setAttribute('style', 'width:'.concat(max_size) + 'px')
        current_health.setAttribute('style', 'width:'.concat(current_health.getAttribute('value') / current_size) + 'px')

        health.replaceChildren((current_health.getAttribute('value') + '/' + health.getAttribute('value')))
    })

}

function flee() {
    let flee = document.querySelector("#flee")

    flee.addEventListener("click", function () {
    })

}

showLogs()
showRankLevel()
showRankVictory()

flee()
attack()