'''

xxxxx
copy this to hw folder since its what we went over in class and comments just needed to be added
xxxxxx

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
        print(f'Difference is {delta.days} days')

        # used to calculate how many years, months, and weeks someone's age is
        delta_years = delta.days // 365.2425

        delta_months = delta.days // 30.14

        delta_weeks = delta.days // 7

       
        #print out the years, months, weeks, days separately from the above calculation
        print(f'You are {delta_years} years old')

        print(f'You are {delta_months} months old')

        print(f'You are {delta_weeks} weeks old')

        print(f'You are {delta.days} days old')


    # raise an error if the directions aren't followed
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()

# 30.14 days in a month