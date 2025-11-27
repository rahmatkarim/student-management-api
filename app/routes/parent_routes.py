from flask import Blueprint
from app.controllers.parent_controller import get_all_parents, create_parent

parent_bp = Blueprint('parent_bp', __name__)

@parent_bp.route('/parents', methods=['GET'])
def index():
    return get_all_parents()

@parent_bp.route('/parents', methods=['POST'])
def store():
    return create_parent()