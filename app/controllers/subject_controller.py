from flask import request, jsonify
from app import db
from app.models.subject import Subject

def get_all_subjects():
    subjects = Subject.query.all()
    return jsonify([s.to_dict() for s in subjects]), 200

def create_subject():
    data = request.get_json()
    new_subject = Subject(
        subject_name=data['subject_name'],
        teacher=data.get('teacher')
    )
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Mapel berhasil ditambah', 'data': new_subject.to_dict()}), 201