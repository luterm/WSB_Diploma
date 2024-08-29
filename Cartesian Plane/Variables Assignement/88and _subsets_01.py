import random

# Create a list to store 88 objects
objects = []

# Generate 88 objects with unique x and y parameters
for _ in range(88):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    objects.append({'x': x, 'y': y})

# Group objects into sets of 5 consecutive x values with the same y value
grouped_objects = []
current_group = []

# Sort the objects based on y and x values
objects.sort(key=lambda obj: (obj['y'], obj['x']))

for obj in objects:
    if not current_group or current_group[-1]['y'] == obj['y']:
        current_group.append(obj)
    else:
        grouped_objects.append(current_group)
        current_group = [obj]

# Add the last group
grouped_objects.append(current_group)

# Display the result
for i, group in enumerate(grouped_objects, 1):
    print(f"Group {i}: {group}")
