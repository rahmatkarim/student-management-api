from app import db

class Grade(db.Model):
    __tablename__ = 'grades'
    
    grade_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    semester = db.Column(db.String(10))
    score = db.Column(db.Numeric(5, 2))
    
    def to_dict(self):
        return {
            'grade_id': self.grade_id,
            'student_id': self.student_id,
            'score': float(self.score),
            'semester': self.semester
        }