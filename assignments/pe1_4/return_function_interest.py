"""

Assignment: Simple Interest Calculator

Objective: 
---------
Write a Python function named calculate_interest that computes and returns the simple interest based on given parameters.

Background
-----------
    - Simple interest is calculated using the formula:

        Simple Interest = (Principal Amount × Rate of Interest × Time) / 100

    - Your task is to translate this formula into a Python function.

Function Requirements
--------------------
    - The function should be named calculate_interest.
    - It should take three parameters:
        1. principal - The principal amount (the initial sum of money).
        2. rate - The rate of interest (as a percentage).
        3. time - The time the money is invested or borrowed for, in years.
    - Get the information from the customer, then call the function and pass the information in. 
    - The function should calculate the simple interest using the given formula and return the result.

Example
--------
    - If you call calculate_interest(1000, 5, 2), the function should return 100.  
        This is because the simple interest on $1000 at a 5% interest rate over 2 years is $100.

Task Instructions
-----------------
1. Define the function calculate_interest with the appropriate parameters.
2. Inside the function, apply the formula to calculate the simple interest.
3. Ensure that the function returns the calculated interest and stores it in a variable named result. 
4. Print the variable, in a user-friendly string, formatted. 
        
        print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                        at an interest rate of {interest_rate}% over a period of \
                        {investment_time} years is: ${calculated_interest:,.2f}")

    - the \ is a symbol you can use to split a string over multiple lines

5. The {principal_amount:,.2f} format specifier formats the principal amount as a floating-point number with two decimal places, 
    and includes commas as thousand separators.
6. The {calculated_interest:,.2f} does the same for the calculated interest.
7. Test your function with different values to ensure it works correctly.

Sample Result:
---------------
Enter the principal amount: 250000
Enter the interest rate as a whole number (5% would be 5): 7
Enter the investment time in whole years: 12
The simple interest for a principal amount of $250,000.00 at an interest rate of 7% over a period of 12 years is: $210,000.00


"""

# calculate the interest

def calculate_interest(principal_amount, interest_rate, investment_time):
    total = (principal_amount * interest_rate * investment_time / 100)
    return total


def main():
        
    principal_amount = 250000
    interest_rate = 7
    investment_time = 12

    result = calculate_interest(principal_amount, interest_rate, investment_time)
    
    print(f"The simple interest for a principal amount of ${principal_amount:,.2f} ")
    print((f"at an interest rate of {interest_rate}% over a period of {investment_time} years is: ${result:,.2f}"))

        
main()
