# statement.md

## Project Title
Student Management System

## Problem Statement
Managing student information manually can make adding, viewing, searching, updating and deleting records difficult. This project demonstrates a simple menu-driven Python solution for student record management.

## Scope
The system manages four student attributes:
- Name
- Roll number
- Course
- Marks

The system provides five record operations:
- Add
- View
- Search
- Update
- Delete

## Target Users
- Students learning Python
- Teachers demonstrating CRUD concepts
- Small academic demonstrations

## Objectives
1. Store student records in a Python list.
2. Use dictionaries to represent individual student records.
3. Use functions to organize operations.
4. Provide a menu-driven workflow.
5. Demonstrate basic CRUD operations.

## Functional Requirements
- The user can add a student.
- The user can view all students.
- The user can search by roll number.
- The user can update a student's name, course and marks.
- The user can delete a student by roll number.
- The user can exit the program.

## Non-Functional Requirements
- Usability: clear text menus and prompts.
- Maintainability: operations are separated into functions.
- Reliability: missing records display "Student not found."
- Simplicity: uses only core Python features.

## Data Storage
Data is stored in memory in:
```python
students = []
```

## Limitation
Records are not persistent. Closing the program clears the list.
