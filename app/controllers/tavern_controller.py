from flask import Blueprint, render_template, flash, url_for, request, redirect
from flask_login import login_required

from ..backend.game.posts_tavern_backend import get_posts, set_posts


tavern = Blueprint('tavern', __name__)


@tavern.route('/tavern', methods=['GET', 'POST'])
@login_required
def home():

    posts = get_posts()

    if request.method == 'POST':

        if set_posts(request.form['text']):
            
            flash('Published!', 'alert-success')
            posts = get_posts()
            return render_template('/game/tavern/tavern.html',
                           title='Tavern Red Boar Inn',
                           posts=posts)

        else:
            flash('Say something!', 'alert-danger')
        
    return render_template('/game/tavern/tavern.html',
                           title='Tavern Red Boar Inn',
                           posts=posts)
