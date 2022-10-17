from flask import Blueprint, render_template, request

from flask_login import login_required

from ..backend.game.arena import Classification, Battle


arena = Blueprint('arena', __name__)


@arena.route('/arena', methods=['GET', 'POST'])
@login_required
def home():

    rank = Classification()
    battle = Battle()
    
    add_html_rank_level = rank.render_by_level()
    add_html_rank_victory = rank.render_by_victory()
    add_html_logs = battle.render_logs()

    online, offline = battle.__len__()

    if request.method == 'POST':        
        battle.shuffle_opponent(choice=request.form.values())
        opponent = battle.render_opponent()
    else:
        opponent = ''

    return render_template('/game/arena/arena.html',
                           title='Arena',
                           offline=offline,
                           online=online,
                           opponent=opponent,
                           add_html_rank_level=add_html_rank_level,
                           add_html_rank_victory=add_html_rank_victory,
                           add_html_logs=add_html_logs)