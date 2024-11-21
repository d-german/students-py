import pandas as pd

from src.core.student_data_service import StudentDataService


class StudentRepository:
    GRADE_POINT_COLUMN = 'grade_point'  # Constant for column name

    def __init__(self, student_data_service: StudentDataService):
        if not student_data_service:
            raise ValueError("student_data_service cannot be None")

        # Convert the students to a DataFrame directly
        self._df = pd.DataFrame([student.__dict__ for student in student_data_service.get_students()])

    def average_grade_point(self) -> float:
        return self._df[self.GRADE_POINT_COLUMN].mean()
