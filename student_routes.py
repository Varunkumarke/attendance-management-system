from flask import Blueprint, request, jsonify
from models import Student, Attendance, db
from datetime import date

student_routes = Blueprint('students', __name__)

@student_routes.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "roll_number": s.roll_number} for s in students])

@student_routes.route('/mark-attendance', methods=['POST'])
def mark_attendance():
    data = request.json  # expects: list of {student_id, status, faculty_id}
    for record in data:
        attendance = Attendance(
            student_id=record['student_id'],
            faculty_id=record['faculty_id'],
            status=record['status'],
            date=date.today()
        )
        db.session.add(attendance)
    db.session.commit()
    return jsonify({"message": "Attendance marked successfully"})
