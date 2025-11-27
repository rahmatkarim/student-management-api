from app import create_app, db
# Import semua model agar terdeteksi oleh SQLAlchemy saat create_all
from app.models.student import Student
from app.models.parent import Parent
from app.models.classes import Classes
from app.models.subject import Subject
from app.models.grade import Grade
from app.models.attendance import Attendance

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Perintah ini akan membuat 6 tabel di database MySQL Anda secara otomatis
        db.create_all()
        print("Database & Tabel berhasil dibuat!")
        
    app.run(debug=True)