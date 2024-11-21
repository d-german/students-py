from dataclasses import dataclass

from src.core.status import Status


@dataclass(frozen=True)
class Student:
    id: int
    first_name: str
    last_name: str
    grade_point: float
    status: Status
