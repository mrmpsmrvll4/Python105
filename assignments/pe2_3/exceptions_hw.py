"""

Objective
--------
Create a custom exception class to handle a specific error scenario in a Python program.

Task
----
Define a new exception class named NotNumericError that inherits from the base Exception class. This exception should be raised when a user inputs an invalid value in a simple input-validation program. Your program should prompt the user to enter a number and raise the InvalidInputError if the input is not a number.

Requirements
------------
1. Implement a custom exception class NotNumericError.
2. Write a Python script that prompts the user to input a number.
3. Use a try-except-else-finally block:
    - The try block should contain the logic to check if the input is a number. (isnumeric() )
    - The except block should catch the InvalidInputError and print an error message.
    - The else block should print a confirmation message if the input is valid.
    - The finally block should print a message indicating the end of the program's execution.
4. Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered. (call the program again)
 

Deliverable
-----------
Submit a Python script (.py file) that implements the custom exception and demonstrates its use with a try-except-else-finally block. The script should handle user input as described and provide appropriate feedback to the user.

Example Code Structure
-----------------------


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


    main()

    
"""

# create a notnumericerror inherited from the exception class
class NotNumericError(Exception):

    # initialize error with default message
    def __init__(self, message="You need to put a number."):
        
        # store the message as an attribute of an error
        self.message = message
        super().__init__(self.message)

    # return the error message when said error is raised
    def __str__(self):
        return f'{self.message}'


def main():

    # make while loop to ask for input until the input is right
    while True:

        try:
            # ask for a number
            value = int(input("Enter a number: "))
            # 
            if value > 9:
                #
                raise NotNumericError()
            

        except NotNumericError as e:
            # handle custom error with printing the custom error
            print(f"error: {e}")


        except Exception as e:
            # handle if it is a different error 
            print(f"The exception is: {e}")
            print("Please enter an integer")
            main()


        else:
            # if no exceptions happen then print the value
            print(f"Correct, you entered {value}.")


        finally:
            # message showing it is all done now
            print("Yee to the haw that's the end of the road pawrtner.")


main()