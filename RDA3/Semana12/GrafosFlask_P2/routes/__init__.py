from .home_routes import home_bp
from .grafos_routes import starter_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(starter_bp)