from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # --- IMPORT ROUTES ---
    from app.routes.student_routes import student_bp
    from app.routes.parent_routes import parent_bp
    from app.routes.classes_routes import classes_bp
    from app.routes.subject_routes import subject_bp
    from app.routes.grade_routes import grade_bp
    from app.routes.attendance_routes import attendance_bp
    
    # --- REGISTER BLUEPRINTS ---
    # Prefix '/api' berarti semua URL akan diawali dengan /api
    # Contoh: /api/students, /api/classes, dll.
    app.register_blueprint(student_bp, url_prefix='/api')
    app.register_blueprint(parent_bp, url_prefix='/api')
    app.register_blueprint(classes_bp, url_prefix='/api')
    app.register_blueprint(subject_bp, url_prefix='/api')
    app.register_blueprint(grade_bp, url_prefix='/api')
    app.register_blueprint(attendance_bp, url_prefix='/api')
    
    return app