
import json


class Repository:

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.items = self.load()

    def load(self):
        try:
            with open(self.filepath,  'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.items, file, indent=4)

    def get_all(self) -> list:
        return self.items

    def get_by_id(self, item_id) -> dict:
        return next((item for item in self.items if item['id'] == item_id), None)

    def get_next_id(self) -> int:
        if len(self.items) == 0:
            return 1
        return max(int(item['id']) for item in self.items) + 1

    def add(self, new_item):
        new_item['id'] = self.get_next_id()
        self.items.append(new_item)
        self.save()

    def update(self, item_id, data):
        item = self.get_by_id(item_id)
        if item is not None:
            item.update(data)
            self.save()
            return item
        return None

    def delete(self, item_id):
        self.items = [
            item for item in self.items if item['id'] != item_id]
        self.save()
