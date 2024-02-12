from flask import Flask, request
from resources import Entry
from entry_manager import EntryManager

app = Flask(__name__)
FOLDER = '/Users/karina/PycharmProjects/toDoBackend'


@app.route("/")
def hello_world():
    return 'Hello, world!'


@app.route("/api/entries/")
def get_entries():
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    entry_list = []
    for item in entry_manager.entries:
        entry_list.append(item.json())
    return entry_list


@app.route("/api/save_entries/", methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    from_request = request.get_json()
    for item in from_request:
        entry = Entry.entry_from_json(item)
        entry_manager.entries.append(entry)
        entry_manager.save()
    return {'result': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
