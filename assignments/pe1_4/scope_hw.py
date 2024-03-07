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