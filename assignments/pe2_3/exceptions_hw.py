"""

Objective
---------
Create a custom exception class to handle a specific error scenario in a Python program.

Task
----
Define a new exception class named InvalidInputError that inherits from the base Exception class.
This exception should be raised when a user inputs an invalid value in a simple input-validation program. 
Your program should prompt the user to enter a number and raise the InvalidInputError if the input is not a number.

Requirements
-----------
Implement a custom exception class InvalidInputError.
Write a Python script that prompts the user to input a number.
Use a try-except-else-finally block:
The try block should contain the logic to check if the input is a number.
The except block should catch the InvalidInputError and print an error message.
The else block should print a confirmation message if the input is valid.
The finally block should print a message indicating the end of the program's execution.
Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered.
 

Deliverable
-----------
Submit a Python script (.py file) that implements the custom exception and demonstrates its use with a try-except-else-finally block. The script should handle user input as described and provide appropriate feedback to the user.

Example Code Structure
----------------------
class InvalidInputError(Exception):
    # Custom exception implementation

def main():
    while True:
        try:
            # Prompt for user input and validate
        except InvalidInputError:
            # Handle invalid input
        else:
            # Confirm valid input
        finally:
            # Indicate end of this iteration

if __name__ == "__main__":
    main()
    

"""


