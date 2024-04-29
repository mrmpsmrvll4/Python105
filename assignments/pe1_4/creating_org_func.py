"""

Assignment: Calculating Factorials

Understanding Factorials
-------------------------
- A factorial is a mathematical operation applied to a non-negative integer n, denoted by n!, 
    that results in the product of all positive integers less than or equal to n. For example, 
    the factorial of 5 (5!) is calculated as 5 x 4 x 3 x 2 x 1, which equals 120.

    
Objective:
----------
- Your task is to write a Python program using a recursive function to calculate the factorial of a number.
    A recursive function is a function that calls itself to solve a problem.


Assignment Instructions
-----------------------
1. Start by defining a function named factorial that takes one parameter, n, 
    representing the number you're calculating the factorial for.
2. In your factorial function, first define the base case. 
    The base case for our recursion will be when n is 1 or 0, because the factorial of 1 and 0 is 1.
3. For the recursive step, if n is greater than 1, 
    the function should return n multiplied by a call to itself with n-1.
4. Create a main function. Inside this function, prompt the user to enter a non-negative integer. 
    Use the int() function to convert the input to an integer.
5. Call the factorial function from your main function with the user's input as its argument, 
    and print the result in a format like "The factorial of n is result.".
6. Finally, call your main function to run the program.


"""

#Calculating Factorials

def factorial(base):
    if base == 1:
        return base
    elif base > 1:
        return base * factorial(base - 1)

# set main def

def main():
    base = int(input("Enter the number: "))
    total_amount = factorial(base)
    print(f"The factorial of {base} is: {total_amount} ")


main()