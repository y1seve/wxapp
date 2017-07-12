from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_user, logout_user
from webapp.models import db, User

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/main'
)

@auth_blueprint.route('/login')
def login():
    render_template('login.html')

@auth_blueprint.route('/authorized')
def authorized():

    wxid = ''
    wx_profile = ''
    wx_nickname = ''

    userQuery = User.query.filter_by(saltid=wxid)
    if userQuery.first():
        userQuery.update({
            'profile': wx_profile,
            'nickname': wx_nickname
        })
        db.session.commit()
    else:
        user = User(wxid, wx_profile, wx_nickname)
        db.session.add(user)
        db.session.commit()
    
    return redirect('')

