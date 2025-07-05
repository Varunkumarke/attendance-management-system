from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    roll_number = db.Column(db.String(20), unique=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    date = db.Column(db.Date, default=date.today)
    status = db.Column(db.String(10))  # 'Present' or 'Absent'
