'''

In this assignment, you will write a Python program that generates a custom calendar for a user's birth month in the current year. 
This task will help you understand how to use Python's Calendar module, interact with users, and display data in a structured format.

Objective
---------
Your program should ask the user for their birth month and then display the calendar for that month in the current year.

Requirements
------------
- Your program must be contained within a main() function.
- Use the Python input() function to ask the user for their birth month (as an integer).
- Ensure your program can handle invalid inputs gracefully.
- Use Python's datetime module to find the current year.
- Generate and display the calendar for the user's birth month in the current year.
- Format the calendar output so it is easy to read and understand.
 

Steps
-----
1. Start by importing the necessary modules: calendar and datetime.
2. Create a main() function where your program's logic will reside.
3. Inside main(), get the current year using datetime.datetime.now().year.
4. Ask the user to enter their birth month and store it in a variable.
5. Validate the user input to ensure it's an integer between 1 and 12.
6. Use the Calendar module to generate the calendar for the given month and year.
7. Print the calendar to the console in a readable format.
8. Don't forget to call the main() function at the end of your script.

'''

from datetime import datetime

from calender import calender

def main():
    print("\n\n")
    print("\n\n")

    today = datetime.datetime.now().year

    question = input("What month is your birth month?  ")



main()