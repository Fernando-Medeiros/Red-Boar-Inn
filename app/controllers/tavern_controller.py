from flask import render_template
from flask_login import login_required


class TavernController:

    @staticmethod
    @login_required
    def home():
        return render_template("game/tavern/tavern.html",
                               title='Tavern')
