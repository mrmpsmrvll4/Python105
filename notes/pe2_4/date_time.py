# calculate a person's age in: Years, months, weeks, days

#
from datetime import datetime

#
def main():
    print("\n\n")
    print("\n\n")
    try:

        #
        today = datetime.today()

        #
        birth_year = int(input("What year were you born?  "))

        #
        month = int(input("What Month were you born (as a number. May would be 5)  "))

        #
        day = int(input("What day of the month were you born?  "))

        #
        birthday = datetime(birth_year, month, day)

        #
        print("Your birthday is: ")

        #
        birthday_output = birthday.strftime("%Y-%m-%d")

        #
        print(birthday_output) 

        #
        delta = today - birthday

        #
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