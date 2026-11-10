"""Unit tests for CampusEngine."""

from campus.engine import CampusEngine, Student, ExamResult


def test_report_card_generator():
    student = Student(student_id="STU-101", student_name="Aditya Nair", grade="Grade 10", roll_number=14)
    results = [
        ExamResult(subject="Mathematics", marks_obtained=92.0),
        ExamResult(subject="Physics", marks_obtained=88.0),
        ExamResult(subject="Chemistry", marks_obtained=84.0),
        ExamResult(subject="English", marks_obtained=90.0),
    ]
    report = CampusEngine.generate_report_card(student, results)

    assert report["student_name"] == "Aditya Nair"
    assert report["percentage"] == 88.5
    assert report["final_grade"] == "A+"
    assert report["result_status"] == "Pass"
