from app import db

class Student(db.Model):
    __tablename__ = 'students'
    
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum('L', 'P'), nullable=False)
    birth_date = db.Column(db.Date)
    address = db.Column(db.String(255))
    
    # Foreign Keys
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.parent_id'))
    
    # Relasi agar bisa memanggil data parent/kelas langsung (Opsional tapi bagus untuk ORM)
    classes_rel = db.relationship('Classes', backref='students')
    parent_rel = db.relationship('Parent', backref='students')

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'gender': self.gender,
            'class_name': self.classes_rel.class_name if self.classes_rel else None, # Ambil nama kelas langsung
            'parent_name': self.parent_rel.name if self.parent_rel else None
        }