
import os
from src.repositories.repository import Repository


class EmployeeRepository(Repository):
    def __init__(self) -> None:
        filepath = os.path.join(os.path.dirname(__file__),
                                '../data/employees.json')
        super().__init__(filepath)
