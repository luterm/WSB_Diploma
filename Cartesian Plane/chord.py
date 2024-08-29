def build_diatonic_chord(maj_scale, notes, start_step, octave_offset=12):
    """
    Build a diatonic chord from the given major scale starting at the specified step.
    
    Parameters:
    maj_scale (list): The major scale notes.
    notes (dict): The dictionary of notes with their Cartesian coordinates.
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
        note_name = maj_scale[chord_index]
        note_coords = notes[note_name]
        
        # Calculate the Cartesian coordinates
        x, y = note_coords
        
        # Apply octave offset for upper structures
        if interval > 7:
            x += octave_offset
            y += octave_offset
        
        chord.append((interval, note_name, (x, y)))
    
    return chord


