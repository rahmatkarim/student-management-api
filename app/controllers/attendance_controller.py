from flask import request, jsonify
from app import db
from app.models.attendance import Attendance

def get_attendance_by_student(student_id):
    att = Attendance.query.filter_by(student_id=student_id).all()
    return jsonify([a.to_dict() for a in att]), 200

def create_attendance():
    data = request.get_json()
    new_attendance = Attendance(
        student_id=data['student_id'],
        date=data['date'], # Format: YYYY-MM-DD
        status=data['status']
    )
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({'message': 'Absensi berhasil dicatat', 'data': new_attendance.to_dict()}), 201