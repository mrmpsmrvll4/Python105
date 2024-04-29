"""

Assignment: Daily Heart Rate Tracker

In this assignment, you will create a Python program to track your daily heart rate. 
The program will record the heart rate at different times of the day and calculate the average heart rate.

Objective:
---------
Create a Python script to track heart rate readings taken at various times throughout the day and calculate the average heart rate.

Requirements:
---------------
1. Define Time Slots:
    - Create a list named time_slots with different times of the day, such as "Morning", "Midday", "Afternoon", "Evening".

2. User Input for Heart Rate:
    - Use a loop to iterate over each time slot. 
        For each time slot, use the input() function to ask the user to enter their heart rate (in beats per minute). 
        Convert this input to an integer.

3. Storing Heart Rate Data:
    - Create an empty list named heart_rates. For each time slot, 
        append a sublist to heart_rates that contains the time slot and the corresponding heart rate.

4. Calculate Average Heart Rate:
    - Initialize a variable to keep track of the total heart rate. Use a loop to add up the heart rate recorded at each time slot. 
        Calculate and print the average heart rate at the end.

Sample Output:
-------------
Enter your heart rate (in BPM) in the Morning: 70 Enter your heart rate (in BPM) at Midday: 75 Enter your heart rate (in BPM) in the Afternoon: 72 Enter your heart rate (in BPM) in the Evening: 68 Average heart rate today: 71.25 BPM


"""

# Time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Store the heart rate data
heart_rates = []

# Loop the time slots to record heart rate
for slot in time_slots:
    # Ask to enter heart rate for the current time slot
    heart_rate_str = input(f"Enter your heart rate (in BPM) in the {slot}: ")
    
    # Convert input to an integer
    heart_rate = int(heart_rate_str)
    
    # Append the time slot and corresponding heart rate to the heart_rates list
    heart_rates.append([slot, heart_rate])

# Calculate total heart rate and count
total_heart_rate = 0
count = 0

# Calculate the total heart rate recorded and count the number of readings
for data in heart_rates:
    total_heart_rate += data[1]
    count += 1

# Calculate average heart rate
average_heart_rate = total_heart_rate / count

# Print the average heart rate
print(f"Average heart rate today: {average_heart_rate} BPM")