import json

notes = {"Anteckning 1": "Text 1", "Anteckning 2":"Text 2"}

with open("notes.json", "w") as f:
    notes = json.dumps(notes)
    f.write(notes)