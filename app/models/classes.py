from app import db

class Classes(db.Model):
    __tablename__ = 'classes'  # Sesuai request nama tabel 'clash'
    
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50), nullable=False)
    homeroom_teacher = db.Column(db.String(100))
    
    def to_dict(self):
        return {
            'class_id': self.class_id,
            'class_name': self.class_name,
            'homeroom_teacher': self.homeroom_teacher
        }