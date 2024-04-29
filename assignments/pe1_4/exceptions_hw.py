"""

Assignment: Adding Exception Handling

Objective: Enhance a basic Python program by implementing try and except statements to handle errors in user input, 
    focusing on data type errors.

Starting Code
-------------

    # Simple Python program to calculate the square of a number

    def square_number():
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

    square_number()
    
Instructions
------------
1. Understand the Code: Review the provided Python script. 
    It calculates the square of a user-input number.
2. Identify Potential Errors: Consider errors that might occur with non-numeric input.
3. Add Exception Handling: Implement try and except blocks to catch a ValueError. 
    Handle incorrect data types with an error message and reprompt.

"""

# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

    except ValueError:
        print("That is not a number. Please enter a number.")

    else:
        print("Thank you for using the square program.")
    
    finally:
        print("Program ended")

square_number()