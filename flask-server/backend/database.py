# # backend/database.py
# import sqlite3
# import hashlib

# class UserDatabase:
#     def __init__(self, db_path='users.db'):
#         self.conn = sqlite3.connect(db_path, check_same_thread=False)
#         self.create_tables()
#         self.initialize_users()

#     def create_tables(self):
#         cursor = self.conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT UNIQUE NOT NULL,
#                 password TEXT NOT NULL,
#                 role TEXT NOT NULL
#             )
#         ''')
#         self.conn.commit()

#     def initialize_users(self):
#         cursor = self.conn.cursor()
        
#         # Check if users exist
#         cursor.execute("SELECT COUNT(*) FROM users")
#         if cursor.fetchone()[0] == 0:
#             # Hash passwords
#             admin_pass = self.hash_password('adminpass')
#             tester_pass = self.hash_password('testerpass')
            
#             # Insert default users
#             users = [
#                 ('admin', admin_pass, 'admin'),
#                 ('tester', tester_pass, 'tester')
#             ]
            
#             cursor.executemany(
#                 'INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
#                 users
#             )
#             self.conn.commit()

#     def hash_password(self, password):
#         return hashlib.sha256(password.encode()).hexdigest()

#     def validate_user(self, username, password):
#         cursor = self.conn.cursor()
#         hashed_password = self.hash_password(password)
        
#         cursor.execute(
#             'SELECT role FROM users WHERE username = ? AND password = ?', 
#             (username, hashed_password)
#         )
#         result = cursor.fetchone()
        
#         return result[0] if result else None

import sqlite3
import hashlib

class UserDatabase:
    def __init__(self, db_path='users.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()
        self.initialize_users()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def initialize_users(self):
        cursor = self.conn.cursor()
        
        # Check if users exist
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            # Hash passwords
            admin_pass = self.hash_password('adminpass')
            tester_pass = self.hash_password('testerpass')
            
            # Insert default users
            users = [
                ('admin', admin_pass, 'admin'),
                ('tester', tester_pass, 'tester')
            ]
            
            cursor.executemany(
                'INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                users
            )
            self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_user(self, username, password):
        cursor = self.conn.cursor()
        hashed_password = self.hash_password(password)
        
        cursor.execute(
            'SELECT role FROM users WHERE username = ? AND password = ?', 
            (username, hashed_password)
        )
        result = cursor.fetchone()
        
        return result[0] if result else None