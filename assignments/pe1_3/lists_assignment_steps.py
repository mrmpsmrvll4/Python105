# Make a program to count the steps and average steps in a week

# Set days of the week
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Set steps of the week
steps= []

# Set total for the week
total = 0
for day in week:
    day_steps = int(input(f"How many steps did you take on {day}: "))
    steps.append(day_steps)
    total += day_steps

# Set the index
index = 0

# Set loop
for day in week:
    print(f"You took {steps[index]} steps on {day} ")
    index += 1

# Set average
average = total / len(steps)

# Print the overall steps and the average steps
print(f"Total Steps: {total}")
print(f"Average steps: {average} ")