import os

from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MyModelView(ModelView):

    def is_accessible(self):
        
        if current_user.is_authenticated:
            if current_user.return_user['email'] == os.environ['ADMIN_EMAIL']:
                return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home.index'))        