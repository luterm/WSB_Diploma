def cartesian_step(note, step_type, direction):
    """
    Calculate the new coordinates based on the step type and direction.
    
    Parameters:
    note (tuple): The current note coordinates (x, y).
    step_type (str): The type of step ('half' or 'whole').
    direction (str): The direction of the step ('up' or 'down').
    
    Returns:
    tuple: The new note coordinates (x, y).
    """
    x, y = note
    
    if step_type == 'half':
        if direction == 'up':
            return (x + 1, y + 1)
        elif direction == 'down':
            return (x - 1, y - 1)
    elif step_type == 'whole':
        if direction == 'up':
            return (x + 1, y + 2)
        elif direction == 'down':
            return (x - 1, y - 2)
    
    raise ValueError("Invalid step type or direction")

# Example usage
note = (3, 4)
print(cartesian_step(note, 'half', 'up'))   # Output: (4, 5)
print(cartesian_step(note, 'whole', 'up'))  # Output: (4, 6)
print(cartesian_step(note, 'half', 'down')) # Output: (2, 3)
print(cartesian_step(note, 'whole', 'down'))# Output: (2, 2)


def musical_intervals(start_note, steps, notes):
    
    """
    Calculate the sequence of notes based on the given steps.
    
    Parameters:
    start_note (tuple): The starting note coordinates (x, y).
    steps (list): A list of tuples where each tuple contains the step type and direction.
                  Example: [('half', 'up'), ('whole', 'down')]
    notes (list): A list of note names corresponding to the Cartesian coordinates.
    
    Returns:
    list: A list of note names after applying the steps.
    """


    current_note = start_note
    result = [notes[current_note[0] % len(notes)]]
    
    for step_type, direction in steps:
        current_note = cartesian_step(current_note, step_type, direction)
        result.append(notes[current_note[0] % len(notes)])
    
    return result

# Example usage
start_note = (3, 4)
steps = [('half', 'up'), ('whole', 'down'), ('half', 'up')]
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']  # Example note set
print(musical_intervals(start_note, steps, notes))  # Output: ['F', 'G', 'E', 'F']