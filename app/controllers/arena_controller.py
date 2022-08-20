from flask import render_template
from flask_login import login_required


class ArenaController:

    @staticmethod
    @login_required
    def home():
        return render_template("arena.html",
                               title='Arena')
