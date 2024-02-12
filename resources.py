import json
from test_json import entry_test


def print_with_indent(value, indent=0):
    indentation = " " * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    @classmethod
    def entry_from_json(cls, value: dict):
        new_entry = cls(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.entry_from_json(item))
        return new_entry

    def save(self, path):
        with open(f'{path}/{self.title}.json', 'w', encoding='urf-8') as f:
            json.dump(self.json(), f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            content = json.load(f)
        return cls.entry_from_json(content)


my_entry1 = Entry("Products")
my_entry2 = Entry("Drinks")
my_entry3 = Entry("Cola")

my_entry1.add_entry(my_entry2)
my_entry2.add_entry(my_entry3)

my_entry1.print_entries()
print()
print(json.dumps(my_entry1.json(), indent=4))

new_entry1 = Entry.entry_from_json(entry_test)
new_entry1.print_entries()
