"""

Assignment: Create a Program to Calculate Areas

Objective: 
----------
Write a Python program that includes two functions - one to calculate the area of a square and another for the area of a circle.

Instructions:
-------------
1. Start with Function Definitions:
    - Begin by defining two functions: square and circle.
    - Each function should take one parameter. For square, name the parameter side. For circle, name it radius.

2. Write the square Function:
    - Inside the square function, calculate the area of a square. Remember, the area of a square is the side length squared (side * side).
    - Use the print function to display the result. The output should be: "The area of the square is [result] square units."
         Replace [result] with the actual calculated area.
    - Make sure to convert the numerical result to a string using str() before concatenating it with other strings.

3. Write the circle Function:
    - In the circle function, calculate the area of a circle using the formula: area = π * radius * radius. You can use 3.14 for π (pi).
    - Display the result using print, similar to the square function. The output should be: "The area of the circle is [result] square units."

4. Test Your Functions:
    - After defining both functions, test them by calling each one with a number of your choice.
    - For example, you can call square(4) and circle(5), but feel free to use any positive numbers.

5. Run Your Program:
    - Execute your program to see the output.
    - Ensure that the output correctly displays the areas for both the square and the circle with the numbers you chose.

Tips:
-----
- Pay attention to the syntax, especially the indentation and the use of parentheses and colons.
- Remember to use the print function to display the results.
    Sample Results: (if you pass 4 and 5, you should use different numbers)

        The area of the square is 16 square units.
        The area of the circle is 78.5 square units.

"""

# area of a circle
def circle(radius):
    area = 3.14 * radius * radius
    print("The area of the circle is " + str(area) + " square units")
    
# area of a square
def square(side):
    area = side * side
    print("The area of the square is " + str(area) + " square units")

# test
circle(8)
square(7)