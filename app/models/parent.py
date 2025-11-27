from app import db

class Parent(db.Model):
    __tablename__ = 'parents'
    
    parent_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    relation = db.Column(db.Enum('Ayah', 'Ibu', 'Wali'), nullable=False)
    
    def to_dict(self):
        return {
            'parent_id': self.parent_id,
            'name': self.name,
            'phone': self.phone,
            'relation': self.relation
        }