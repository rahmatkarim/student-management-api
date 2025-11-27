from app import db

class Subject(db.Model):
    __tablename__ = 'subjects'
    
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100))
    
    def to_dict(self):
        return {
            'subject_id': self.subject_id,
            'subject_name': self.subject_name,
            'teacher': self.teacher
        }