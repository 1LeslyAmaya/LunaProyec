from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/inicio')
@login_required
def inicio():
    return f"<h2>Bienvenido, {current_user.username} </h2><p>Ya estás dentro de Luna.</p>"
