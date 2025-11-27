from flask import Blueprint
from app.controllers.classes_controller import get_all_classes, create_class

classes_bp = Blueprint('classes_bp', __name__)

@classes_bp.route('/classes', methods=['GET'])
def index():
    return get_all_classes()

@classes_bp.route('/classes', methods=['POST'])
def store():
    return create_class()