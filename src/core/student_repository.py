import pandas as pd

from src.core.status import Status
from src.core.student import Student
from src.core.student_data_service import StudentDataService


class StudentRepository:
    ID_COLUMN = 'id'
    FIRST_NAME_COLUMN = 'first_name'
    LAST_NAME_COLUMN = 'last_name'
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

    def top_n_students(self, n: int) -> list[Student]:
        # Sort the DataFrame by grade point in descending order
        sorted_df = self._df.sort_values(by=self.GRADE_POINT_COLUMN, ascending=False)

        # Select the top N rows
        top_n_df = sorted_df.head(n)

        # Convert the resulting rows back to a list of Student objects
        top_n_students = [
            Student(
                id=row[self.ID_COLUMN],
                first_name=row[self.FIRST_NAME_COLUMN],
                last_name=row[self.LAST_NAME_COLUMN],
                grade_point=row[self.GRADE_POINT_COLUMN],
                status=row[self.STATUS_COLUMN]
            )
            for _, row in top_n_df.iterrows()  # _ is the index, row is the row data, we don't need the index
        ]

        return top_n_students
