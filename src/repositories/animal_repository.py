import json
import os


class AnimalRepository:
    def __init__(self) -> None:
        path = os.path.join(os.path.dirname(
            __file__), '../data/animals.json')
        self.filepath = path
        self.animals = self.load_animals()

    def load_animals(self):
        try:
            with open(self.filepath,  'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_animals(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.animals, file, indent=4)

    def get_all(self):
        return self.animals

    def get_by_id(self, animal_id):
        return next((animal for animal in self.animals if animal['id'] == animal_id), None)

    def add(self, new_animal):
        self.animals.append(new_animal)
        self.save_animals()

    def update(self, animal_id, data):
        animal = self.get_by_id(animal_id)
        if animal is not None:
            animal.update(data)
            self.save_animals()
            return animal
        return None

    def delete(self, animal_id):
        self.animals = [
            animal for animal in self.animals if animal['id'] != animal_id]
        self.save_animals()
