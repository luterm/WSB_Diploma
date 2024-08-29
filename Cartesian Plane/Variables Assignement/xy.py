import random

database = {
    'F##': (1, 1),  'G':   (2, 1),  'Abb':  (3, 1),
    'G#':  (2, 2),  'Ab':  (3, 2),
    'G##': (2, 3),  'A':   (3, 3),  'Bbb': (4, 3),
    'A#':  (3, 4),  'Bb':  (4, 4),  'Cbb': (5, 4),
    'A##': (3, 5),  'B':   (4, 5),  'Cb':  (5, 5),
    'B#':  (4, 6),  'C':   (5, 6),  'Dbb': (6, 6),
    'B##': (4, 7),  'C#':  (5, 7),  'Db':  (6, 7),
    'C##': (5, 8),  'D':   (6, 8),  'Ebb': (7, 8),
    'D#':  (6, 9),  'Eb':  (7, 9),  'Fbb': (8, 9), 
    'D##': (6, 10), 'E':   (7, 10), 'Fb':  (8, 10),
    'E#':  (7, 11), 'F':   (8, 11), 'Gbb': (9, 11),
    'E##': (7, 12), 'F#':  (8, 12), 'Gb':  (9, 12),

    'F##2': (8, 13),  'G2':  (9, 13),  'Abb2': (10, 13),
    'G#2':  (9, 14),  'Ab2': (10, 14),
    'G##2': (9, 15),  'A2':  (10, 15), 'Bbb2': (11, 15),
    'A#2':  (10, 16), 'Bb2': (11, 16), 'Cbb2': (12, 16),
    'A##2': (10, 17), 'B2':  (11, 17), 'Cb2':  (12, 17),
    'B#2':  (11, 18), 'C2':  (12, 18), 'Dbb2': (13, 18),
    'B##2': (11, 19), 'C#2': (12, 19), 'Db2':  (13, 19),
    'C##2': (12, 20), 'D2':  (13, 20), 'Ebb2': (14, 20),
    'D#2':  (13, 21), 'Eb2': (14, 21), 'Fbb2': (15, 21),
    'D##2': (13, 22), 'E2':  (14, 22), 'Fb2':  (15, 22),
    'E#2':  (14, 23), 'F2':  (15, 23), 'Gbb2': (16, 23),
    'E##2': (14, 24), 'F#2': (15, 24), 'Gb2':  (16, 24),

    'F##3': (15, 25), 'G3':  (16, 25), 'Abb3': (17, 25),
    'G#3':  (16, 26), 'Ab3': (17, 26),
    'G##3': (16, 27), 'A3':  (17, 27), 'Bbb3': (18, 27),
    'A#3':  (17, 28), 'Bb3': (18, 28), 'Cbb3': (19, 28),
    'A##3': (17, 29), 'B3':  (18, 29), 'Cb3':  (19, 29),
    'B#3':  (18, 30), 'C3':  (19, 30), 'Dbb3': (20, 30),
    'B##3': (18, 31), 'C#3': (19, 31), 'Db3':  (20, 31),
    'C##3': (19, 32), 'D3':  (20, 32), 'Ebb3': (21, 32),
    'D#3':  (20, 33), 'Eb3': (21, 33), 'Fbb3': (22, 33),
    'D##3': (20, 34), 'E3':  (21, 34), 'Fb3':  (22, 34),
    'E#3':  (21, 35), 'F3':  (22, 35), 'Gbb3': (23, 35),
    'E##3': (21, 36), 'F#3': (22, 36), 'Gb3':  (23, 36),
}

'''keys = list(database.keys())
def print_keys_in_groups(keys, group_size=12):
    for i in range(0, len(keys), group_size):
        print(', '.join(keys[i:i + group_size]))'''
"""print(keys)  # Prints: ['a', 'A', 'b', 'B']
print(database)  # Prints the entire dictionary: {'a': (1, 1), 'A': (2, 2), 'b': (3, 3), 'B': (4, 4)}
for key in keys:
    print(key)  # Prints each key: 'a', 'A', 'b', 'B'"""
#print_keys_in_groups(keys)


# Reverse lookup dictionary for coordinates
coord_to_note = {v: k for k, v in database.items()}

def get_major_scale(start_note):
    """
    Generate the major scale starting from the given note.
    """
    steps = [(1, 2), (1, 2), (1, 1), (1, 2), (1, 2), (1, 2), (1, 1)]
    maj_scale = [start_note]
    current_x, current_y = database[start_note]

    for step in steps:
        current_x += step[0]
        current_y += step[1]
        next_note = coord_to_note.get((current_x, current_y))
        if next_note:
            maj_scale.append(next_note)
        else:
            print(f"Note not found for coordinates ({current_x}, {current_y})")
            break

    return maj_scale

def print_major_scale_with_roman_numerals(maj_scale):
    """
    Print the major scale with Roman numerals in a single line.
    """
    roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
    formatted_scale = ', '.join(f"{roman_numerals[i]}: {note}" for i, note in enumerate(maj_scale))
    print(formatted_scale)

# Main execution
if __name__ == "__main__":
    # Get user input
    start_note = input("Enter the starting note: ")

    # Validate user input
    if start_note not in database:
        print("Invalid note. Please choose a valid note from the database.")
    else:
        # Get the major scale
        maj_scale = get_major_scale(start_note)
        print("Major scale starting from {}:".format(start_note))
        print_major_scale_with_roman_numerals(maj_scale)



def build_diatonic_chord(maj_scale, start_step, octave_offset=12):
    """
    Build a diatonic chord from the given major scale starting at the specified step.
    
    Parameters:
    maj_scale (list): The major scale notes.
    start_step (int): The step of the scale to start the chord (1-based index).
    octave_offset (int): The offset to apply for the upper octave notes.
    
    Returns:
    list: The diatonic chord elements with intervals and coordinates.
    """
    chord_intervals = [1, 3, 5, 7, 9, 11, 13]
    chord = []
    scale_length = len(maj_scale)
    
    # Convert start_step to 0-based index
    start_index = start_step - 1
    
    for i, interval in enumerate(chord_intervals):
        # Calculate the index of the chord element
        chord_index = (start_index + i * 2) % scale_length
        note = maj_scale[chord_index]
        
        # Calculate the Cartesian coordinates
        x = chord_index
        y = interval
        
        # Apply octave offset for upper structures
        if interval > 7:
            x += octave_offset
            y += octave_offset
        
        chord.append((interval, note, (x, y)))
    
    return chord

# Example usage
#maj_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
start_step = input("Enter the starting step (Roman numeral): ")
roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
start_step_index = roman_numerals.index(start_step.upper()) + 1
diatonic_chord = build_diatonic_chord(maj_scale, start_step_index)
print("Diatonic chord starting from step {}:".format(start_step))
for interval, note, coords in diatonic_chord:
    print("{} - {} at {}".format(interval, note, coords))