import os

from src.repositories.repository import Repository


class RevenueRepository(Repository):
    def __init__(self):
        filepath = os.path.join(os.path.dirname(__file__),
                                '../data/revenue.json')
        super().__init__(filepath)
