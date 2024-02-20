# Months in a year
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Days in a month
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Set loop
for i in range(len(months)):
    month = months[i]

    days = num_of_days[i]

# tabbed since it is part of the loop and to print the loop   
    print(f"{month} has {days} days")