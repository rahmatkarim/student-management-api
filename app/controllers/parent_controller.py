from flask import request, jsonify
from app import db
from app.models.parent import Parent

def get_all_parents():
    parents = Parent.query.all()
    return jsonify([p.to_dict() for p in parents]), 200

def create_parent():
    data = request.get_json()
    new_parent = Parent(
        name=data['name'],
        phone=data.get('phone'),
        address=data.get('address'),
        relation=data['relation']
    )
    db.session.add(new_parent)
    db.session.commit()
    return jsonify({'message': 'Data orang tua berhasil ditambah', 'data': new_parent.to_dict()}), 201