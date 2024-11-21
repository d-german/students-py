from core.status import Status
from core.student import Student
from core.student_data_service import StudentDataService


def main():
    students = [
        Student(id=1, first_name="John", last_name="Doe", grade_point=4, status=Status.ACTIVE),
        Student(id=2, first_name="Jane", last_name="Doe", grade_point=3, status=Status.INACTIVE),
    ]

    service = StudentDataService(students)
    print(service.get_students())

    student = Student(id=1, first_name="John", last_name="Doe", grade_point=4, status=Status.ACTIVE)
    print(student.__dict__)


if __name__ == '__main__':
    main()
