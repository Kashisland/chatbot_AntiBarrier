# ../db/db_config.py

import pymysql
import os

DB_USERNAME = os.getenv("DB_USERNAME", "dbadmin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "asdf1234")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "capstone_db")

# 데이터베이스 연결 함수
def get_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
