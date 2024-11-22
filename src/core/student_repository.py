import pandas as pd

from src.core.status import Status
from src.core.student_data_service import StudentDataService


class StudentRepository:
    GRADE_POINT_COLUMN = 'grade_point'
    STATUS_COLUMN = 'status'

    def __init__(self, student_data_service: StudentDataService):
        if not isinstance(student_data_service, StudentDataService):
            raise ValueError("student_data_service must be an instance of StudentDataService")

        self._df = pd.DataFrame([student.__dict__ for student in student_data_service.get_students()])

    def highest_grade_point(self) -> float:
        return self._df[self.GRADE_POINT_COLUMN].max()

    def lowest_grade_point(self) -> float:
        return self._df[self.GRADE_POINT_COLUMN].min()

    def average_grade_point(self, status: Status = None) -> float:
        if status:
            filtered_df = self._df[self._df[self.STATUS_COLUMN] == status]
            if filtered_df.empty:
                return 0.0
            return filtered_df[self.GRADE_POINT_COLUMN].mean()

        return self._df[self.GRADE_POINT_COLUMN].mean()
