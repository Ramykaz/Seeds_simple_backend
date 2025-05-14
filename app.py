from flask import Flask, jsonify, abort

app = Flask(__name__)

# --- Mock Data (from previous steps) ---
students_db = {
    "student1": {"name": "Ali Hassan", "enrolled_course_ids": ["course101", "course201"]},
    "student2": {"name": "Layla Ibrahim", "enrolled_course_ids": ["course201"]},
    "student3": {"name": "Omar Yusuf", "enrolled_course_ids": ["course301"]},
}

teachers_db = {
    "teacherA": {"name": "Fatima Ahmed", "taught_course_ids": ["course101", "course301"]},
    "teacherB": {"name": "Youssef El Masry", "taught_course_ids": ["course201"]},
}

courses_db = {
    "course101": {
        "title": "Beginner's Tajweed",
        "description": "Learn the fundamental rules of Tajweed.",
        "teacher_id": "teacherA",
        "student_ids": ["student1"]
    },
    "course201": {
        "title": "Arabic Language for Beginners",
        "description": "Master the Arabic alphabet and basic vocabulary.",
        "teacher_id": "teacherB",
        "student_ids": ["student1", "student2"]
    },
    "course301": {
        "title": "Qur'an Memorization (Juzz Amma)",
        "description": "Guided memorization of the last Juzz.",
        "teacher_id": "teacherA",
        "student_ids": ["student3"]
    },
}
# --- End of Mock Data ---


# Endpoint 1: List courses for a specific student
@app.route('/students/<string:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    student = students_db.get(student_id)
    if not student:
        abort(404, description=f"Student with ID '{student_id}' not found.")

    enrolled_course_ids = student.get("enrolled_course_ids", [])
    student_courses = []

    for course_id in enrolled_course_ids:
        course_info = courses_db.get(course_id)
        if course_info:
            teacher_name = teachers_db.get(course_info.get("teacher_id"), {}).get("name", "N/A")
            student_courses.append({
                "id": course_id,
                "title": course_info.get("title"),
                "description": course_info.get("description"),
                "teacher_name": teacher_name
            })

    return jsonify({
        "student_id": student_id,
        "student_name": student.get("name"),
        "courses": student_courses
    })


# Endpoint 2: List courses taught by a specific teacher
@app.route('/teachers/<string:teacher_id>/courses', methods=['GET'])
def get_teacher_courses(teacher_id):
    teacher = teachers_db.get(teacher_id)
    if not teacher:
        abort(404, description=f"Teacher with ID '{teacher_id}' not found.")

    taught_course_ids = teacher.get("taught_course_ids", [])
    teacher_courses = []

    for course_id in taught_course_ids:
        course_info = courses_db.get(course_id)
        if course_info:
            # For each course, we can list the enrolled students' names
            enrolled_student_names = []
            for student_id_in_course in course_info.get("student_ids", []):
                student_detail = students_db.get(student_id_in_course)
                if student_detail:
                    enrolled_student_names.append(student_detail.get("name"))

            teacher_courses.append({
                "id": course_id,
                "title": course_info.get("title"),
                "description": course_info.get("description"),
                "enrolled_students_count": len(course_info.get("student_ids", [])),
                "enrolled_student_names": enrolled_student_names # Optional: list student names
            })


    return jsonify({
        "teacher_id": teacher_id,
        "teacher_name": teacher.get("name"),
        "courses_taught": teacher_courses
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)
