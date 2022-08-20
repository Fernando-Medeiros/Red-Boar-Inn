from flask import render_template
from flask_login import login_required


class SettingsController:

    @staticmethod
    @login_required
    def home():
        return render_template("settings.html",
                               title='Settings')
