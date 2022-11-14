from flask import Blueprint, render_template
from flask_login import login_required

from ..backend.game.equipment import Equipments
from ..backend.game.profile import Profile
from ..backend.game.status import CraftSkills, Status
from ..backend.game.vocation import Vocation

profile = Blueprint('profile', __name__)


tmp_folder = 'game/profile/'
tmp_folder_sub = 'game/profile/sub/'



@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def home():
    
    profile = Profile()

    return render_template(tmp_folder + 'profile.html',
                           title='profile')



@profile.route('/profile/vocation', methods=['GET', 'POST'])
@login_required
def vocation():

    vocation = Vocation()
    add_html_vocations = vocation.render_vocation()

    return render_template(tmp_folder_sub + 'vocation.html',
                           title='Vocation',
                           add_html_vocations=add_html_vocations)



@profile.route('/profile/job', methods=['GET', 'POST'])
@login_required
def job():
    return render_template(tmp_folder_sub + 'job.html',
                           title='Job')



@profile.route('/profile/status', methods=['GET', 'POST'])
@login_required
def status():

    status = Status()
    craft_skills = CraftSkills()

    add_html_status = status.render_status()
    add_html_craft_skills = craft_skills.render_craft_skills()

    return render_template(tmp_folder_sub + 'status.html',
                           title='Status',
                           add_html_status=add_html_status,
                           add_html_craft_skills=add_html_craft_skills)



@profile.route('/profile/skills', methods=['GET', 'POST'])
@login_required
def skills():
    return render_template(tmp_folder_sub + 'skills.html',
                           title='Skills')


@profile.route('/profile/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template(tmp_folder_sub + 'settings.html',
                           title='Settings')



@profile.route('/profile/equipment', methods=['GET', 'POST'])
@login_required
def equipment():
    
    equipment = Equipments()
    dict_equipments = equipment.dict_equipments()

    return render_template(tmp_folder_sub + 'equipment.html',
                           title='Equipment',
                           dict_equipments=dict_equipments)