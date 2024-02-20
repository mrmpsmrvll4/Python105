
# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Create an empty list to store heart rate data
heart_rates = []

# Loop through each time slot to record heart rate
for slot in time_slots:
    # Ask user to enter heart rate for the current time slot
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