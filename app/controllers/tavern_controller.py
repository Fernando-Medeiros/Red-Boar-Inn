from flask import Blueprint, render_template, flash, url_for, request, redirect
from flask_login import login_required

from ..backend.game.posts_tavern_backend import get_posts, set_posts


tavern = Blueprint('tavern', __name__)


@tavern.route('/tavern', methods=['GET', 'POST'])
@login_required
def home():

    posts = get_posts()
    html = [] 

    for post in posts.__reversed__():
        
        sprite = url_for('static', filename='img/sprites/' + post['sprite'])

        html.append(
            f"""
            <div class="body-posts">

                <div class="column-img-name-date">
                    <img src="{sprite}" width="50px">
                    <span> { post['charname'].title() } </span>
                    <small> { post['date'][:10] } </small>
                    <small> { post['date'][10:] } </small>
                </div>

                <div class="post-info">
                    { post['info'] }
                </div>
            </div>
            """)

    add_html = "\n".join(html)


    if request.method == 'POST':

        if set_posts(request.form['text']):
            
            flash('Published!', 'alert-success')
            
            return redirect(url_for('tavern.home'))

        else:
            flash('Say something!', 'alert-danger')

    return render_template('/game/tavern/tavern.html',
                           title='Tavern Red Boar Inn',
                           add_html=add_html)
