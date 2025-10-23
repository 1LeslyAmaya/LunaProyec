from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/inicio')
@login_required
def inicio():
    return render_template('inicio.html')

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/inicio')
@login_required
def inicio():
    return render_template('inicio.html', current_user=current_user)

# === NUEVA RUTA PERFIL ===
@main.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', user=current_user)
