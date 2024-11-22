import pytest

from src.core.status import Status
from src.core.student import Student
from src.core.student_data_service import StudentDataService
from src.core.student_repository import StudentRepository


# Test data
@pytest.fixture
def sample_students():
    return [
        Student(id=1, first_name="John", last_name="Doe", grade_point=4.0, status=Status.ACTIVE),
        Student(id=2, first_name="Jane", last_name="Smith", grade_point=3.5, status=Status.INACTIVE),
        Student(id=3, first_name="Alice", last_name="Brown", grade_point=3.0, status=Status.ACTIVE),
    ]


@pytest.fixture
def repository(sample_students):
    data_service = StudentDataService(sample_students)
    return StudentRepository(data_service)


def test_init():
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        StudentRepository(None)

    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        StudentRepository('wrong type')


def test_highest_grade_point(repository):  # "test_" is a pytest convention to identify test functions
    assert repository.highest_grade_point() == 4.0


def test_lowest_grade_point(repository):
    assert repository.lowest_grade_point() == 3.0


def test_average_grade_point(repository):
    assert repository.average_grade_point() == 3.5


def test_average_grade_point_by_status(repository):
    assert repository.average_grade_point(Status.ACTIVE) == 3.5
    assert repository.average_grade_point(Status.INACTIVE) == 3.5
    assert repository.average_grade_point(Status.GRADUATED) == 0.0


def test_top_n_students(repository):
    top_students = repository.top_n_students(2)
    assert len(top_students) == 2
    assert top_students[0].id == 1
    assert top_students[1].id == 2
    assert top_students[0].grade_point == 4.0
    assert top_students[1].grade_point == 3.5
