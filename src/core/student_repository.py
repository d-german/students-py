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
            # Extract the 'status' column from the DataFrame
            status_column = self._df[self.STATUS_COLUMN]

            # Create a boolean mask for rows where the status matches the given status
            matching_status_mask = status_column == status

            # Filter the DataFrame based on the boolean mask
            filtered_df = self._df[matching_status_mask]

            # Check if the filtered DataFrame is empty
            if filtered_df.empty:
                return 0.0

            # Calculate the average grade point for the filtered rows
            return filtered_df[self.GRADE_POINT_COLUMN].mean()

        # If no status is provided, calculate the overall average grade point
        return self._df[self.GRADE_POINT_COLUMN].mean()
