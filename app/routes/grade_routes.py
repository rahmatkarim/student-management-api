from flask import Blueprint
from app.controllers.grade_controller import create_grade, get_grades_by_student

grade_bp = Blueprint('grade_bp', __name__)

@grade_bp.route('/grades', methods=['POST'])
def store():
    return create_grade()

# Contoh URL: /api/grades/student/1 (Melihat nilai siswa ID 1)
@grade_bp.route('/grades/student/<int:student_id>', methods=['GET'])
def show_by_student(student_id):
    return get_grades_by_student(student_id)