from logic import (
    add_student_record,
    search_student_record,
    update_student_record,
    delete_student_record,
)


def test_add_student():
    students = []
    add_student_record(students, "Amit", "101", "BCA", "85")
    assert len(students) == 1
    assert students[0]["name"] == "Amit"


def test_search_student():
    students = []
    add_student_record(students, "Amit", "101", "BCA", "85")
    result = search_student_record(students, "101")
    assert result["course"] == "BCA"


def test_search_missing_student():
    assert search_student_record([], "999") is None


def test_update_student():
    students = []
    add_student_record(students, "Amit", "101", "BCA", "85")
    assert update_student_record(students, "101", "Rahul", "BTech", "90")
    assert students[0]["name"] == "Rahul"
    assert students[0]["marks"] == "90"


def test_delete_student():
    students = []
    add_student_record(students, "Amit", "101", "BCA", "85")
    assert delete_student_record(students, "101")
    assert students == []
