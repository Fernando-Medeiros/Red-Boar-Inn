from flask import render_template
from flask_login import login_required


class CharacterController:

    @staticmethod
    @login_required
    def home():
        return render_template("game/character/character.html",
                               title='Character')
