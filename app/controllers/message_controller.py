from flask import Blueprint, flash, redirect, render_template, request, url_for
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