# Seeds Platform - Basic Backend API (Python/Flask)

This project is a simple backend API built with Python and Flask for the "Seeds Roles Assignment." It provides endpoints to retrieve course information related to students and teachers.

## Assignment Focus: Task 2 - Backend (Python)

The primary goal of this task was to create a basic backend system with two specific API endpoints:
1.  An endpoint for listing courses per student.
2.  An endpoint for listing courses per teacher.

## Features

*   **Mock Data:** Uses in-memory Python dictionaries to simulate a database for students, teachers, and courses.
*   **Two API Endpoints:**
    *   `GET /students/<student_id>/courses`: Retrieves all courses a specific student is enrolled in.
    *   `GET /teachers/<teacher_id>/courses`: Retrieves all courses a specific teacher teaches, including a list of enrolled students for each course.
*   **JSON Responses:** All endpoints return data in JSON format.
*   **Error Handling:** Returns appropriate 404 errors if a student or teacher ID is not found.

## Technologies Used

*   **Python 3**
*   **Flask:** A lightweight WSGI web application framework in Python.
*   **Virtual Environment (`venv`):** For managing project dependencies.

## Project Structure
seeds-backend/
├── venv/                   # Virtual environment directory
├── app.py                  # Main Flask application file with routes and logic
└── README.md               

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd seeds-backend
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv  # Or python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # .\venv\Scripts\activate    # On Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install Flask
    ```
4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The application will start on `http://127.0.0.1:5001` by default (as configured in `app.py`).

## API Endpoints

### 1. Get Courses for a Student

*   **URL:** `/students/<student_id>/courses`
*   **Method:** `GET`
*   **URL Params:**
    *   `student_id` (string, required): The ID of the student.
*   **Success Response (200 OK):**
    ```json
    {
      "student_id": "student1",
      "student_name": "Ali Hassan",
      "courses": [
        {
          "id": "course101",
          "title": "Beginner's Tajweed",
          "description": "Learn the fundamental rules of Tajweed.",
          "teacher_name": "Fatima Ahmed"
        },
        {
          "id": "course201",
          "title": "Arabic Language for Beginners",
          "description": "Master the Arabic alphabet and basic vocabulary.",
          "teacher_name": "Youssef El Masry"
        }
      ]
    }
    ```
*   **Error Response (404 Not Found):**
    ```json
    {
        "description": "Student with ID 'student_unknown' not found."
    }
    ```
*   **Example API Call (using `curl`):**
    ```bash
    curl http://127.0.0.1:5001/students/student1/courses
    ```

### 2. Get Courses for a Teacher

*   **URL:** `/teachers/<teacher_id>/courses`
*   **Method:** `GET`
*   **URL Params:**
    *   `teacher_id` (string, required): The ID of the teacher.
*   **Success Response (200 OK):**
    ```json
    {
      "teacher_id": "teacherA",
      "teacher_name": "Fatima Ahmed",
      "courses_taught": [
        {
          "id": "course101",
          "title": "Beginner's Tajweed",
          "description": "Learn the fundamental rules of Tajweed.",
          "enrolled_students_count": 1,
          "enrolled_student_names": ["Ali Hassan"]
        },
        {
          "id": "course301",
          "title": "Qur'an Memorization (Juzz Amma)",
          "description": "Guided memorization of the last Juzz.",
          "enrolled_students_count": 1,
          "enrolled_student_names": ["Omar Yusuf"]
        }
      ]
    }
    ```
*   **Error Response (404 Not Found):**
    ```json
    {
        "description": "Teacher with ID 'teacher_unknown' not found."
    }
    ```
*   **Example API Call (using `curl`):**
    ```bash
    curl http://127.0.0.1:5001/teachers/teacherA/courses
    ```

## Further Development (Potential) I can do the following

*   Integrate with a proper database (e.g., SQLite, PostgreSQL).
*   Add POST, PUT, DELETE methods for managing resources.
*   Implement authentication and authorization.

