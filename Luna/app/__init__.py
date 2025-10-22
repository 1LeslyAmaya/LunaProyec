from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'luna-secret-key'

    # Importar y registrar las rutas principales
    from app.routes.main_routes import main
    app.register_blueprint(main)

    return app
