from utils import musical_intervals

def generate_major_scale(start_note, notes):
    # Define the steps for a major scale in terms of Cartesian steps
    steps = [('whole', 'up'), ('whole', 'up'), ('half', 'up'), ('whole', 'up'), 
             ('whole', 'up'), ('whole', 'up'), ('half', 'up')]
    
    # Generate the major scale
    scale = musical_intervals(start_note, steps, notes)
    
    return scale

def print_major_scale_with_roman_numerals(scale):
    roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
    for i, note in enumerate(scale):
        print(f"{roman_numerals[i % len(roman_numerals)]}: {note}")

# Example usage
if __name__ == "__main__":
    start_note = (3, 4)
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']  # Example note set
    maj_scale = generate_major_scale(start_note, notes)
    print("Major scale starting from {}:".format(start_note))
    print_major_scale_with_roman_numerals(maj_scale)
