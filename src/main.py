from core.status import Status
from core.student import Student


def main():
    student = Student(
        id=1,
        first_name="John",
        last_name="Doe",
        grade_point=3.5,
        status=Status.GRADUATED
    )

    print(student)


if __name__ == '__main__':
    main()
