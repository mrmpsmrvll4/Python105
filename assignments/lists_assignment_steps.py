#more list notes and examples

week = ["Sunday", "Monday", "tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Sort the week list in ascending order
week.sort()

# sort the week list in descending order
week.reverse()

print("Days of the week (in descending order):", week)

#remove "Sunday" from the list
week.remove("Sunday")

steps= []

total = 0
for day in week:
    day_steps = int(input(f"How many steps did you take on {day}: "))
    steps.append(day_steps)
    total += day_steps

index = 0

for day in week:
    print(f"On {day} you took {steps[index]} steps.")
    index += 1

average = total / len(steps)
print(f"You walked an average of {average:.1f} steps per day.")