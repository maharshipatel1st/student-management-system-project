# Student Management System - Python Console Project

## 1. Project Overview
This project is a simple **Student Management System** implemented in Python using a list of dictionaries and functions.

The implementation follows the provided program structure:
- `students = []`
- `add_student()`
- `view_students()`
- `search_student()`
- `update_student()`
- `delete_student()`
- A menu-driven `while True` main program

## 2. Functional Modules
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

## 3. Data Structure
Each student is stored as a Python dictionary:

```python
{
    "name": name,
    "roll_no": roll_no,
    "course": course,
    "marks": marks
}
```

All dictionaries are stored inside the `students` list.

## 4. Requirements
- Python 3.x
- No external package is required to run the main program.

## 5. How to Run

```bash
python student_management.py
```

Then select an option from 1 to 6.

## 6. Testing
The `tests/` folder contains pytest tests for the core CRUD logic.

Optional test installation:
```bash
pip install pytest
pytest -q
```

## 7. Important Limitation
The supplied code stores data only in memory. When the program is closed, student records are lost. No database or file storage was added because this project is intentionally based on the provided Python code.

## 8. Future Enhancements
- Save records to a file or database.
- Add marks validation.
- Prevent duplicate roll numbers.
- Add student attendance.
- Add report generation.
- Add a graphical interface.
