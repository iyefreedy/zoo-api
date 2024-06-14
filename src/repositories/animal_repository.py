
import os
from src.repositories.repository import Repository


class AnimalRepository(Repository):
    def __init__(self) -> None:
        current_directory = os.path.dirname(__file__)
        filepath = os.path.join(current_directory, '../data/animals.json')
        super().__init__(filepath)
