from flask import request, jsonify
from app import db
from app.models.grade import Grade

def get_grades_by_student(student_id):
    grades = Grade.query.filter_by(student_id=student_id).all()
    return jsonify([g.to_dict() for g in grades]), 200

def create_grade():
    data = request.get_json()
    new_grade = Grade(
        student_id=data['student_id'],
        subject_id=data['subject_id'],
        semester=data['semester'],
        score=data['score']
    )
    db.session.add(new_grade)
    db.session.commit()
    return jsonify({'message': 'Nilai berhasil diinput', 'data': new_grade.to_dict()}), 201