1user_hours = (input("Enter hours:"))
user_min = (input("Enter minutes:"))

print(type(user_hours))
print(type(user_min))

user_hours = int(user_hours)
user_min = int(user_min)

print(type(user_hours))
print(type(user_min))

while user_min >= 60:
    user_hours += 1
    user_min -= 60

print("Working time:", user_hours, "hours and", user_min, "minutes.")
quit()


# basic version
user_hours = (1)
user_min = (80)

while user_min >= 60:
    user_hours += 1
    user_min -= 60

work = (user_hours, user_min)

print (work)
