import json

def load_counter():
    try:
        with open('data/counter.json', 'r') as file:
            return json.load(file)
    except FileNotFoundEror:
        return 0

def save_counter(counter):
    with open('data/counter.json', 'w') as file:
        json.dump(counter, file)
