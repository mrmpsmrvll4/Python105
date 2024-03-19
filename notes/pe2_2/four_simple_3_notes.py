# Numbers Processor.

# Prompt the user to enter a line of numbers separated by spaces.
line = input("Enter a line of numbers - separate them with spaces: ")

# Split the input line into individual number strings based on spaces.
strings = line.split()

# Initialize a variable to store the total sum of numbers.
total = 0

# Try block to handle potential errors during the conversion of strings to floats.
try:
    # Iterate over each number string extracted from the input line.
    for substr in strings:
        # Convert each number string to a float and add it to the total.
        total += float(substr)
    
    # If the conversion and summation are successful, print the total.
    print("The total is:", total)

# Except block to handle exceptions that might occur during the conversion or summation.
except:
    # If an exception occurs, print a message indicating the problematic substring.
    print(substr, "is not a number.")