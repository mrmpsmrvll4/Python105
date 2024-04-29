"""

Assignment:
Intermediate Tutorial: Creating and Using Python Modules and Packages

This tutorial is designed for students who have completed the first Python Essentials class and are familiar with if-statements, loops, and Visual Studio Code. 
You will learn how to create and use Python modules and packages.

Step 1: Creating a Python Module
    a. Create a new folder named modules in Visual Studio Code then create a new file named calculator.py.
    Add the following code to calculator.py:
    b.

        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

c. Save the file (Ctrl+S).

Step 2: Using the Module in Another Script
    a. Create a new Python file in the same folder, named main.py.
        In main.py, import the calculator module and use its functions:
    b.

        import calculator

        result = calculator.add(5, 3)
        print("Addition result:", result)

        result = calculator.subtract(10, 4)
        print("Subtraction result:", result)

c. Save and run main.py to see the results of the addition and subtraction functions.

Step 3: Organizing Code into Packages
    a. Create a new folder in your project named math_operations.
        Move the calculator.py file into the math_operations folder.
    c. Inside math_operations, create an empty file named __init__.py. 
        This file turns the folder into a Python package.
    d. Update main.py to import the module from the package:
    b.

        from math_operations import calculator

        # rest of your code...
Step 4: Exploring More Advanced Package Concepts
    Add another module to your math_operations package: geometry.py for geometric calculations.  
    Calculate the area of a rectangle, triangle, and circle. This will give you a practical understanding
    of how larger Python projects are organized into modules and packages.

xxxxxxx
the modules folder
xxxxxxxx




"""