import os
from src.repositories.repository import Repository


class FeedingRepository(Repository):
    def __init__(self) -> None:
        filepath = os.path.join(os.path.dirname(__file__),
                                '../data/feedings.json')
        super().__init__(filepath)
