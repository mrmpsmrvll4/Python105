# List of months in a year
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Corresponding list of the number of days in each month
# Note: This list ignores leap years for February
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Iterate through each month using a for loop
for i in range(len(months)):
    month = months[i]

    # Retrieve the number of days from the num_of_days list
    days = num_of_days[i]

    # Print the month and its corresponding number of days
    # using the f formatting prevents a problem from concatenating the num_of_days which are integers into the string
    print(f"{month} has {days} days")
    
    # This loop steps through each index from 0 to 11 (for 12 months)
    # and uses the index to access elements from both lists.