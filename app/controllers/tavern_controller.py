from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from ..backend.game.tavern import Tavern

tavern = Blueprint('tavern', __name__)


@tavern.route('/tavern', methods=['GET', 'POST'])
@login_required
def home():

    tavern_posts = Tavern()

    add_html = tavern_posts.render_posts()

    if request.method == 'POST':

        if tavern_posts.add_post(request.form['text']):
            
            flash('Published!', 'alert-success')
            
            return redirect(url_for('tavern.home'))

        else:
            flash('Say something!', 'alert-danger')
    
    return render_template('/game/tavern/tavern.html',
                           title='Tavern Red Boar Inn',
                           add_html=add_html)
