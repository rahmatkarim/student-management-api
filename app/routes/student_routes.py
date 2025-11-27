from flask import Blueprint
from app.controllers.student_controller import (
    get_all_students, 
    create_student, 
    get_student_by_id, 
    delete_student
)

student_bp = Blueprint('student_bp', __name__)

# Definisi Endpoints
@student_bp.route('/students', methods=['GET'])
def index():
    return get_all_students()

@student_bp.route('/students', methods=['POST'])
def store():
    return create_student()

@student_bp.route('/students/<int:id>', methods=['GET'])
def show(id):
    return get_student_by_id(id)

@student_bp.route('/students/<int:id>', methods=['DELETE'])
def destroy(id):
    return delete_student(id)