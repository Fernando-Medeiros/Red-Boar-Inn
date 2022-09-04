from flask import render_template

from app.models.user import User, Characters
from app.updates import dic_updates


class HomeController:

    @staticmethod
    def home():
        try:
            length_users = User.length()
            rank_characters_by_level = Characters.length()[:10]
        except:
            length_users = 0
            rank_characters_by_level = [0, 0]

        return render_template("home/home/home.html",
                               title='Home - Flask Rpg',
                               rank_characters_by_level=rank_characters_by_level,
                               length_users=length_users)

    @staticmethod
    def updates():

        updates_notes = dic_updates[:10]

        return render_template("home/updates/updates.html",
                               title='Updates',
                               updates_notes=updates_notes)

    @staticmethod
    def about():
        return render_template("home/about/about.html",
                               title='About us')
