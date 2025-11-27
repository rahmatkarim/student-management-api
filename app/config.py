import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# 1. Load file .env
load_dotenv()

class Config:
    # 2. Ambil data dari file .env
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    
    # 3. Handle password jika mengandung karakter aneh
    if DB_PASS:
        encoded_password = quote_plus(DB_PASS)
    else:
        encoded_password = ''

    # 4. Susun link koneksi
    # Format: mysql+mysqlconnector://USER:PASS@HOST:PORT/DB_NAME
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_kunci')