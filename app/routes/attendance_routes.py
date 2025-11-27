from flask import Blueprint
from app.controllers.attendance_controller import create_attendance, get_attendance_by_student

attendance_bp = Blueprint('attendance_bp', __name__)

@attendance_bp.route('/attendance', methods=['POST'])
def store():
    return create_attendance()

@attendance_bp.route('/attendance/student/<int:student_id>', methods=['GET'])
def show_by_student(student_id):
    return get_attendance_by_student(student_id)