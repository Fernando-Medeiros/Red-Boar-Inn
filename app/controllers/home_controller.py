from flask import render_template

from app.models.user import User


class HomeController:

    @staticmethod
    def home():
        length_users = len(User.query.all())

        return render_template("home/home/home.html",
                               title='Home - Flask Rpg',
                               length_users=length_users)

    @staticmethod
    def updates():

        with open('updates.txt', mode='r', encoding='utf-8') as read_updates:
            updates_notes = read_updates.readlines()

        return render_template("home/updates/updates.html",
                               updates_notes=updates_notes,
                               title='Updates')

    @staticmethod
    def about():
        return render_template("home/about/about.html",
                               title='About us')
