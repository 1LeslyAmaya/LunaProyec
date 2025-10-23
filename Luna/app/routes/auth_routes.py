from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

# === REGISTRO ===
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Verificar si el correo ya existe
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('⚠️ Este correo ya está registrado. Intenta con otro.', 'danger')
            return redirect(url_for('auth.register'))

        # Crear nuevo usuario
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_pw)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('✅ Usuario registrado exitosamente. Inicia sesión ahora.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            print(f"Error al registrar usuario: {e}")
            flash('❌ Ocurrió un error al registrar el usuario.', 'danger')

    return render_template('register.html')


# === LOGIN ===
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False  # "Recordarme"

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)
            flash('✅ Inicio de sesión exitoso.', 'success')
            return redirect(url_for('main.inicio'))  # Redirige al panel principal
        else:
            flash('❌ Correo o contraseña incorrectos.', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')


# === LOGOUT ===
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('👋 Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))
