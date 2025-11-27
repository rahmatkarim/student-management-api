from flask import request, jsonify
from app import db
from app.models.classes import Classes

def get_all_classes():
    classes = Classes.query.all()
    return jsonify([c.to_dict() for c in classes]), 200

def create_class():
    data = request.get_json()
    new_class = Classes(
        class_name=data['class_name'],
        homeroom_teacher=data.get('homeroom_teacher')
    )
    db.session.add(new_class)
    db.session.commit()
    return jsonify({'message': 'Kelas berhasil dibuat', 'data': new_class.to_dict()}), 201