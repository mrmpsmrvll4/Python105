"""

BMI Calculator Assignment:

Objective: Create a BMI calculator that takes a user's weight and height, 
    calculates their BMI, and then categorizes their BMI into underweight, normal weight, overweight, or obese.

Requirements:
-------------
1. This should be done inside of a main function. The conversion variables should be above main because they are global. 
2. Input:
    1. Ask the user to enter their weight in pounds.
    2. Ask the user to enter their height in inches.
3. Conversion to Metric:
    These variables should be global and constant (at the top of the page and ALL CAPS) 
        1. Convert weight from pounds to kilograms (1 pound = 0.453592 kilograms).
        2. Convert height from inches to meters (1 inch = 0.0254 meters).
4. BMI Calculation:
    1. Calculate the BMI using the formula: bmi = weight (kg) / (height (m) * height (m)).
    2. Ensure the calculation is done using metric units.
5. BMI Categories:
    1. Underweight: bmi < 18.5
    2. Normal weight: 18.5 ≤ bmi < 24.9
    3. Overweight: 25 ≤ bmi < 29.9
    4. Obese: bmi ≥ 30
6. Output:
    1. Display the calculated BMI with two decimal places.
    2. Display the BMI category based on the calculated BMI.
7. Error Checking:
    1. Check for valid numerical inputs. 
        Handle any invalid inputs with an appropriate message and prompt for re-entry.
8. Documentation:
    1. Comment the code to explain different sections or important lines.
        Sample Results:
            Enter your weight in pounds: 154
            Enter your height in inches: 68
            Your BMI is: 23.43
            You are in the normal weight category.


"""

# createa a bmi calculator using scope

global KG
KG = 0.453592

global M
M = 0.0254


def calculate_bmi(weight, height):
    calculate_bmi = weight * (KG) / (height * (M) * height * (M))
    print(calculate_bmi)
    get_bmi_category(calculate_bmi)


def main():
        input_weight = int( input(f"Please enter your weight in pounds:  ") )
    
        input_height = int( input(f"Please enter your height in inches:  ") )
    
        print(f"Your BMI is{()} ")

        calculate_bmi(input_weight,input_height)


def get_bmi_category(calculate_bmi):
    if calculate_bmi < 18.5:
         print("underweight")
    elif calculate_bmi <= 24.9:
        print("normal weight")
    elif calculate_bmi <= 25:
        print("overweight")
    else:
        print("obese")

main()