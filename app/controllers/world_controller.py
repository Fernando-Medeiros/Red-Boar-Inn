from flask import render_template
from flask_login import login_required


class WorldController:

    @staticmethod
    @login_required
    def home():
        return render_template("world.html",
                               title='World')
