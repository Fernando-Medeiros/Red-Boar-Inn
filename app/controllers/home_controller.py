from flask import render_template


class HomeController:

    @staticmethod
    def home():
        return render_template("home.html",
                               title='Home - Flask Rpg')

    @staticmethod
    def updates():

        with open('app/updates.txt', mode='r', encoding='utf-8') as read_updates:
            updates_notes = read_updates.readlines()

        return render_template("home_views/updates.html",
                               updates_notes=updates_notes,
                               title='Updates')

    @staticmethod
    def about():
        return render_template("home_views/about.html",
                               title='About us')
