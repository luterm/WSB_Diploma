import json
from scale import generate_major_scale, print_major_scale_with_roman_numerals

def load_notes(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return list(data["notes"].keys())  # Extract note names from the "notes" key

# Example usage
start_note = input("Enter the starting note: ")
notes = load_notes('notes.json')
maj_scale = generate_major_scale(start_note, notes)
print("Major scale starting from {}:".format(start_note))
print_major_scale_with_roman_numerals(maj_scale)