from flask import render_template
from flask_login import login_required


class ProfileController:

    @staticmethod
    @login_required
    def home():
        return render_template("game/profile/profile.html",
                               title='Profile')
