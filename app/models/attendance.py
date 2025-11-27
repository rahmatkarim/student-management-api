from app import db

class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    attendance_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    date = db.Column(db.Date)
    status = db.Column(db.Enum('present', 'absent', 'late', 'excused'))
    
    def to_dict(self):
        return {
            'attendance_id': self.attendance_id,
            'student_id': self.student_id,
            'date': str(self.date),
            'status': self.status
        }