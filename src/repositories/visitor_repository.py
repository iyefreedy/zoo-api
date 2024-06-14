import os

from src.repositories.repository import Repository


class VisitorRepository(Repository):
    def __init__(self):
        filepath = os.path.join(os.path.dirname(__file__),
                                '../data/visitors.json')
        super().__init__(filepath)
