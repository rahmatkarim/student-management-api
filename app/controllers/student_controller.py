from flask import request, jsonify
from app import db
# Import model yang dibutuhkan
from app.models.student import Student
from app.models.parent import Parent
from app.models.classes import Classes

def get_all_students():
    try:
        students = Student.query.all()
        # Menggunakan list comprehension untuk format JSON
        return jsonify([s.to_dict() for s in students]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_student():
    data = request.get_json()
    
    # Validasi input wajib
    if not data or 'name' not in data or 'class_id' not in data:
        return jsonify({'message': 'Data tidak lengkap (name, class_id wajib)'}), 400

    # Buat object baru
    new_student = Student(
        name=data['name'],
        gender=data['gender'],
        birth_date=data.get('birth_date'), # Format YYYY-MM-DD
        address=data.get('address'),
        class_id=data['class_id'],
        parent_id=data.get('parent_id')
    )
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Siswa berhasil ditambahkan', 'data': new_student.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Gagal menambahkan data', 'error': str(e)}), 500

def get_student_by_id(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Siswa berhasil dihapus'}), 200