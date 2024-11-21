from typing import List

from src.core.student import Student


class StudentDataService:
    def __init__(self, students: List['Student']):  # Specify that students is a list of Student objects
        self._students = students

    def get_students(self) -> List['Student']:  # The method returns a list of Student objects
        return self._students
