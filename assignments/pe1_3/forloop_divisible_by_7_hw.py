"""

Python Assignment: 
----------------
Find Numbers Divisible by 7


In this assignment, you will write a Python program to identify and print all the numbers divisible by 7 that fall between 1 and 300. 
This task will help you practice using loops and conditional statements in Python.


Objective:
---------
Your program should iterate through the numbers 1 to 300. For each number, it should check if the number is divisible by 7. A number is divisible by 7 if the remainder is 0 when the number is divided by 7. This can be checked using the modulus operator (%) in Python.


Requirements:
-------------
- Use a for loop to iterate through the range of numbers from 1 to 300.
- Inside the loop, use an if statement to check if a number is divisible by 7. To do this, use the modulus operator (%) and compare the remainder with 0.
- If a number is divisible by 7, print that number.
- Ensure your program outputs each qualifying number on a separate line.


Example Output:
---------------
    - If your program is working correctly, the beginning of your output should look like this:

        7
        14
        21
        28
        ...


"""

# Iterate through the numbers from 1 to 300
for num in range(1, 301):
    # Check if the number is divisible by 7
    if num % 7 == 0:
        # If divisible by 7, print the number
        print(num)