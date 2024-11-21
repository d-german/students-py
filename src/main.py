from core.status import Status
from core.student import Student
from core.student_data_service import StudentDataService
from src.core.student_repository import StudentRepository


def main():
    service = StudentDataService([
        Student(id=1, first_name="John", last_name="Doe", grade_point=4, status=Status.ACTIVE),
        Student(id=2, first_name="Jane", last_name="Doe", grade_point=3, status=Status.INACTIVE),
    ])
    print(service.get_students())

    print(StudentRepository(service).average_grade_point())


if __name__ == '__main__':
    main()
