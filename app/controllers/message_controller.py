from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


message = Blueprint('message', __name__)



@message.route('/message', methods=['GET', 'POST'])
@login_required
def home():
  
    return render_template('game/message/message.html',
                           title='Messages')



@message.route('/friend', methods=['GET'])
@login_required
def friend():
  
    return render_template('game/message/friend.html',
                           title='Friends')



@message.route('/notification', methods=['GET'])
@login_required
def notification():
  
    return render_template('game/message/notification.html',
                           title='Notifications')