# Step 1: Define a function to get user input for worker name, hours, and minutes.
# Step 2: Validate the input to ensure hours and minutes are integers.
# Step 3: Summarize the total time in hours and minutes.
# Step 4: Store the summarized time in a table (dictionary) with the worker's name as the key.
# Step 5: Define a function to display the table upon user request.
# Step 6: Create a loop to allow the user to enter time for different workers and to display the table.

# Import necessary library
import sys

# Initialize a table to store time summaries
time_summary_table = {}

def get_time_input():
    worker_name = input("Enter worker's name: ")
    try:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
    except ValueError:
        print("Please enter valid integers for hours and minutes.")
        return None, None, None
    return worker_name, hours, minutes

def summarize_time(hours, minutes):
    total_hours = hours + minutes // 60
    total_minutes = minutes % 60
    return total_hours, total_minutes
2
def add_to_table(worker_name, hours, minutes):
    if worker_name in time_summary_table:
        current_hours, current_minutes = time_summary_table[worker_name]
        total_hours, total_minutes = summarize_time(current_hours + hours, current_minutes + minutes)
    else:
        total_hours, total_minutes = summarize_time(hours, minutes)
    time_summary_table[worker_name] = (total_hours, total_minutes)

def display_table():
    print("Time Summary Table:")
    for worker, time in time_summary_table.items():
        print(f"{worker}: {time[0]} hours, {time[1]} minutes")

def main():
    while True:
        print("\nOptions: 1 - Add time, 2 - Display table, 3 - Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            worker_name, hours, minutes = get_time_input()
            if worker_name is not None:
                add_to_table(worker_name, hours, minutes)
        elif choice == '2':
            display_table()
        elif choice == '3':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()