"""

Assignment: 
-----------
Basic Logical Operations with Integers


In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts the user for two integer inputs and then demonstrates the use of these operators.

1. User Input: Start by asking the user to input two distinct integers. 
2. Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
    - and
    - or
    - not
3. Display Results: For each comparison, print both the logical statement and its result.
4. Guidelines for Logical Comparisons:
    - Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
    - Try to use comparisons that could yield different results based on user input.

    Sample Output: 
        - Here's an example of what your program's output might look like:
 

            Enter an integer: 5
            Enter another integer: 6
            Both numbers greater than 0:  True
            Both numbers greater than 100:  False
            Either number is even?  True
            Either number is less than 100?   True
            num1 is not equal to num2:  True
            num1 is not 0:  True



"""

#ask the user for two integer inputs
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#and
print("Both numbers greater than 5:", num1 >5 and num2 > 5)
print("Both numbers greater than 50:", num1 > 50 and num2 > 50)

#or
print("Either number is odd?", num1 % 2 != 0 or num2 % 2 != 0)
print("Either number is less than 50?", num1 < 50 or num2 < 50)

#not
print("num2 is not equal to num1:", num2 != num1)
print("num1 is not 5:", not num1 == 5)