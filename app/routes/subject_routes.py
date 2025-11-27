from flask import Blueprint
from app.controllers.subject_controller import get_all_subjects, create_subject

subject_bp = Blueprint('subject_bp', __name__)

@subject_bp.route('/subjects', methods=['GET'])
def index():
    return get_all_subjects()

@subject_bp.route('/subjects', methods=['POST'])
def store():
    return create_subject()