from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from ..backend.game.equipment_backend import equipments


profile = Blueprint('profile', __name__)


tmp_folder = 'game/profile/'
tmp_folder_sub = 'game/profile/sub/'



@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def home():

    return render_template(tmp_folder + 'profile.html',
                           title='profile')



@profile.route('/profile/vocation', methods=['GET', 'POST'])
@login_required
def vocation():

    return render_template(tmp_folder_sub + 'vocation.html',
                           title='Vocation')



@profile.route('/profile/job', methods=['GET', 'POST'])
@login_required
def job():

    return render_template(tmp_folder_sub + 'job.html',
                           title='Job')



@profile.route('/profile/status', methods=['GET', 'POST'])
@login_required
def status():

    return render_template(tmp_folder_sub + 'status.html',
                           title='Status')



@profile.route('/profile/skills', methods=['GET', 'POST'])
@login_required
def skills():

    return render_template(tmp_folder_sub + 'skills.html',
                           title='Skills')



@profile.route('/profile/craft_skills', methods=['GET', 'POST'])
@login_required
def craft_skills():

    return render_template(tmp_folder_sub + 'craft_skills.html',
                           title='Craft Skills')



@profile.route('/profile/settings', methods=['GET', 'POST'])
@login_required
def settings():

    return render_template(tmp_folder_sub + 'settings.html',
                           title='Settings')



@profile.route('/profile/equipment', methods=['GET', 'POST'])
@login_required
def equipment():
  
    add_html = equipments()

    return render_template(tmp_folder_sub + 'equipment.html',
                           title='Equipment',
                           add_html=add_html)