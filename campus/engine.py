"""Education Campus & Student Academic Management Engine for Frappe."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class Student(BaseModel):
    student_id: str
    student_name: str
    grade: str  # Class 10, Grade 12, B.Tech Sem 4
    section: str = "A"
    roll_number: int


class FeeStructure(BaseModel):
    academic_year: str
    tuition_fee: float
    lab_fee: float = 0.0
    library_fee: float = 0.0
    bus_fee: float = 0.0


class ExamResult(BaseModel):
    subject: str
    max_marks: float = 100.0
    marks_obtained: float


class CampusEngine:
    """Manages student enrollments, fee invoicing, and grade cards."""

    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.fee_structures: Dict[str, FeeStructure] = {}

    def calculate_total_fee(self, grade: str) -> float:
        fee = self.fee_structures.get(grade)
        if not fee:
            return 45000.0  # default
        return fee.tuition_fee + fee.lab_fee + fee.library_fee + fee.bus_fee

    @staticmethod
    def generate_report_card(student: Student, results: List[ExamResult]) -> Dict[str, Any]:
        total_max = sum(r.max_marks for r in results)
        total_obtained = sum(r.marks_obtained for r in results)
        percentage = (total_obtained / total_max * 100.0) if total_max > 0 else 0.0

        if percentage >= 85:
            grade_letter = "A+"
        elif percentage >= 70:
            grade_letter = "A"
        elif percentage >= 55:
            grade_letter = "B"
        elif percentage >= 40:
            grade_letter = "C"
        else:
            grade_letter = "F"

        return {
            "student_id": student.student_id,
            "student_name": student.student_name,
            "grade": student.grade,
            "total_marks": total_obtained,
            "max_marks": total_max,
            "percentage": round(percentage, 2),
            "final_grade": grade_letter,
            "result_status": "Pass" if percentage >= 40 else "Fail",
        }
