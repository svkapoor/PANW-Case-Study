import json
import os

# Makes path to entries.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),  # PANW-CASE-STUDY/journal/
    "..",                       # PANW-CASE-STUDY
    "data",                     # PANW-CASE-STUDY/data
    "entries.json"              # PANW-CASE-STUDY/data/entries.json
)

def load_entries():
    """
    Load the list of entries from entries.json.
    Returns a list of dictionaries.
    """
    with open(DATA_PATH, "r") as f:
        try:
            data = json.load(f) # turns json to python object
            if isinstance(data, list):
                return data
            return []   # if somehow corrupted
        except json.JSONDecodeError:
            return []   # JSON file is empty or broken

def save_entry(entry_dict):
    """
    Append one new entry (as a dictionary) to the JSON file.
    """
    entries = load_entries()      # load existing entries
    entries.append(entry_dict)    # add new entry

    # Write entire updated list back to the file
    with open(DATA_PATH, "w") as f:
        json.dump(entries, f, indent=2)
