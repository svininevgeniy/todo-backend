from resources import Entry
import os


class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for item in self.entries:
            item.save(self.data_path)

    def load(self):
        for item in os.listdir(self.data_path):
            full_path = os.path.join(self.data_path, item)
            if full_path.endswith('.json'):
                entry = Entry.load(full_path)
                self.entries.append(entry)

    def add_entry(self, title: str):
        entry = Entry(title)
        self.entries.append(entry)


grocery_list = Entry('Limes')
grocery_list.print_entries()
