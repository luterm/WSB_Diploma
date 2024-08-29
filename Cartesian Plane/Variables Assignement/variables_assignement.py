import random

# Step 1: Initialize the 12 Variables
# We'll store these in a dictionary where keys are variable names, and values are (x, y) tuples.
data_base = {
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

    'f##': (8, 13),  'g':  (9, 13),  'abb': (10, 13),
    'g#':  (9, 14),  'ab': (10, 14),
    'g##': (9, 15),  'a':  (10, 15), 'bbb': (11, 15),
    'a#':  (10, 16), 'bb': (11, 16), 'cbb': (12, 16),
    'a##': (10, 17), 'b':  (11, 17), 'cb':  (12, 17),
    'b#':  (11, 18), 'c':  (12, 18), 'dbb': (13, 18),
    'b##': (11, 19), 'c#': (12, 19), 'db':  (13, 19),
    'c##': (12, 20), 'd':  (13, 20), 'ebb': (14, 20),
    'd#':  (13, 21), 'eb': (14, 21), 'fbb': (15, 21),
    'd##': (13, 22), 'e':  (14, 22), 'fb':  (15, 22),
    'e#':  (14, 23), 'f':  (15, 23), 'gbb': (16, 23),
    'e##': (14, 24), 'f#': (15, 24), 'gb':  (16, 24),
    'f##': (15, 25), 'g':  (16, 25), 'abb': (17, 25)
}

# Step 2: Create a function to handle user input and assign one of the 12 variables
def assign_variable(user_input, chosen_variable):
    if 1 <= user_input <= 7:
        assignment[user_input] = data_base[chosen_variable]
        print(f"Assigned {chosen_variable} -> Position {user_input}: {data_base[chosen_variable]}")
    else:
        print("Invalid input! Please enter a number between 1 and 7.")

# Initialize an assignment dictionary to store the user assignments
assignment = {}

# Simulate user input
user_input = int(input("Enter a number between 1 and 7: "))
chosen_variable = input("Enter a variable name (e.g., 'var1', 'var2', etc.): ")
assign_variable(user_input, chosen_variable)

# Step 3: Random Assignment Function
def random_assignment():
    for i in range(1, 8):  # We have 7 possible user inputs (1 to 7)
        random_var = random.choice(list(data_base.keys()))
        assignment[i] = data_base[random_var]
        print(f"Randomly assigned {random_var} -> Position {i}: {data_base[random_var]}")

# Simulate random assignment
random_assignment()

# Step 4: Display the Final Assignment
print("\nFinal Assignments:")
for key, value in assignment.items():
    print(f"Position {key}: {value}")


    #consider using another, lower count of variables to modify them on the fly if needed