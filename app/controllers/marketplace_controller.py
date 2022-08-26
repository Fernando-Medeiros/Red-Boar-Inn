from flask import render_template
from flask_login import login_required


class MarketplaceController:

    @staticmethod
    @login_required
    def home():
        return render_template("game/marketplace/marketplace.html",
                               title='Marketplace')
