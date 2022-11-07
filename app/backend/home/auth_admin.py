from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for



class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.return_user['email'] == 'fernandobasilides@gmail.com'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home.index'))        