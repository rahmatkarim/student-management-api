# Student Management API

**Proyek Ujian Tengah Semester (UTS) - Pemrograman Web Lanjut**

Aplikasi REST API berbasis **Python Flask** untuk sistem manajemen data siswa, nilai, dan absensi sekolah. Proyek ini dibangun menggunakan arsitektur **MVC (Model-View-Controller)** dan database **MySQL** yang terintegrasi dengan layanan cloud (Filess.io).

## 🛠 Teknologi

* **Bahasa:** Python 3.10+
* **Framework:** Flask
* **Database:** MySQL (Cloud)
* **ORM:** SQLAlchemy
* **Tools:** Postman, Git

## 🚀 Fitur Utama

1.  **Manajemen Siswa:** Create, Read, Update, Delete (CRUD) data siswa.
2.  **Data Induk:** Pengelolaan data Kelas, Wali Kelas, dan Orang Tua.
3.  **Akademik:** Input Nilai Mata Pelajaran dan Absensi Harian.
4.  **Keamanan:** Koneksi database aman menggunakan Environment Variable (.env).

## ⚙️ Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer Anda:

**1. Clone Repository**
Unduh source code proyek ini ke komputer lokal Anda.

**2. Install Library**
Install semua kebutuhan sistem menggunakan perintah:
`pip install -r requirements.txt`

**3. Konfigurasi Database**
Buat file bernama `.env` dan masukkan data koneksi database Filess.io Anda (Host, User, Password, Database Name).

**4. Start Server**
Jalankan aplikasi dengan perintah:
`python run.py`

## 📡 Dokumentasi API

Gunakan aplikasi **Postman** untuk mengakses alamat-alamat berikut:

### 🏫 Data Master

| Method | Endpoint | Fungsi |
| :--- | :--- | :--- |
| **POST** | `/api/classes` | Menambah data kelas baru |
| **POST** | `/api/parents` | Menambah data orang tua |
| **POST** | `/api/subjects` | Menambah mata pelajaran |

### 👨‍🎓 Data Siswa

| Method | Endpoint | Fungsi |
| :--- | :--- | :--- |
| **GET** | `/api/students` | Melihat seluruh data siswa |
| **POST** | `/api/students` | Mendaftarkan siswa baru |
| **GET** | `/api/students/<id>` | Melihat detail siswa per ID |
| **DELETE** | `/api/students/<id>` | Menghapus siswa dari sistem |

### 📝 Transaksi Akademik

| Method | Endpoint | Fungsi |
| :--- | :--- | :--- |
| **POST** | `/api/grades` | Memasukkan nilai siswa |
| **POST** | `/api/attendance` | Mencatat absensi kehadiran |
| **GET** | `/api/grades/student/<id>` | Melihat transkrip nilai siswa |

## 👤 Author

**Nama:** Rahmat Karim Matdoan
**NIM:** 21.83.0669
**Prodi:** Teknik Komputer
**Kampus:** UNIVERSITAS AMIKOM YOGYAKARTA

