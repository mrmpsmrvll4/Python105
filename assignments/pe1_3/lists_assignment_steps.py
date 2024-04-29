"""

Assignment
 ---------
 Assigning Steps

Welcome to your Python assignment! This task will help you practice working with lists, user input, and basic calculations. 

Follow the steps below:
-----------------------
1. Create a List: Start by creating a list named days that includes all seven days of the week.
2. Initialize an Empty List: Create an empty list called steps. This will store the number of steps taken each day.
3. User Input: Using a loop, ask the user to enter the number of steps they took for each day, based on your days list. 
    For example, "How many steps did you take on Monday?"
4. Store Steps: Append the user's input (number of steps) to the steps list for each day.
5. Display Daily Steps: Show the user the steps recorded for each day.
6. Total Steps: Calculate and display the total number of steps taken in the week.
7. Average Steps: Create a variable named average to calculate the average steps taken. 
    Use the formula: average = round(total / len(steps)). Display the average steps.
 

Sample Result:
--------------

How many steps did you take on Sunday? 5468
How many steps did you take on Monday? 6587
How many steps did you take on Tuesday? 9786
How many steps did you take on Wednesday? 6875
How many steps did you take on Thursday? 6854
How many steps did you take on Friday? 5876
How many steps did you take on Saturday? 5874

You took 5468 steps on Sunday
You took 6587 steps on Monday
You took 9786 steps on Tuesday
You took 6875 steps on Wednesday
You took 6854 steps on Thursday
You took 5876 steps on Friday
You took 5874 steps on Saturday


Total steps:  47320
Average steps:  6760


"""

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