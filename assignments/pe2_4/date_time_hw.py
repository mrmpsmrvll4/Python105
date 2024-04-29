'''

Python Datetime Assignment: Age Calculator
 

In this assignment, you will create a program that asks the user for their birthday and then calculates their age in different units such as years, months, days, hours, and minutes. This exercise will help you practice using the datetime and timedelta modules in Python.

Assignment Objectives:
----------------------
- Ask the user to input their birthday.
- Calculate the user's age in years, months, days, hours, and minutes.
- Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
- Display the results in a user-friendly format.
- Implement the solution inside a main() function.

Instructions:
-------------
Create a Python script that performs the following steps:

1. Define a main() function where your program logic will reside.
2. Use my start program from GitHub: startprogramLinks to an external site.
You can view the classroom demonstration of how we got to the code at the top of the page.
3. Comment explaining each line of the code
    1.Finish the code to get and display:
        1. months
        2. weeks
        3. days (done)
        4. years (done)
4. Format and print the results in a clear, understandable manner.

Tips:
-----
- To calculate the age in years, you might need to consider leap years. A simple approach is to divide the total number of days by 365.25.
- For months, first calculate the years, then use the remaining days to estimate the months.
- For weeks, calculate by dividing days by 7
- Use try-except blocks to handle any potential input errors.
 

Sample Output:
--------------
What year were you born?  1971
What Month were you born (as a number. May would be 5)  5
What day of the month were you born?  16
Your birthday is: 
1971-05-16
Difference is 19338 days
You are 52.0 years old

'''


# calculate a person's age in: Years, months, weeks, days

# import the datetime module for times and dates
from datetime import datetime


def main():

    print("\n\n")
    print("\n\n")

    try:

        # today's date
        today = datetime.today()


        # ask for the user's year they were born
        birth_year = int(input("What year were you born?  "))

        # ask for the user's month they were born
        month = int(input("What Month were you born (as a number. May would be 5)  "))

        # ask for the user's day they were born
        day = int(input("What day of the month were you born?  "))


        # create an object for the overall birthday
        birthday = datetime(birth_year, month, day)

        # print the birhday in the right format
        print("Your birthday is: ")


        # set the birthday in year - month - day format
        birthday_output = birthday.strftime("%Y-%m-%d")

        # print out the new output from above
        print(birthday_output) 


        # the math for the difference between the user's birthday and today
        delta = today - birthday

        # print out the math from above in a readable format
        print(f'It has been {delta.days} days since you were born.')


        # used to calculate how many years, months, and weeks someone's age is
        delta_years = delta.days // 365.2425

        delta_months = delta.days // 30.14

        delta_weeks = delta.days // 7

       
        #print out the years, months, weeks, days separately from the above calculation
        print(f'Which means you are {delta.days} days old')

        print(f'You are {delta_years} years old')

        print(f'You are {delta_months} months old')

        print(f'and you are {delta_weeks} weeks old')


    # raise an error if the directions aren't followed
    except Exception as e:
        print(f"Uh oh spaghetti o's!!!:  {e}")
        
        # call main to run the code back and restart if exception is raised 
        main()


main()