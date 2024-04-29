"""


Assignment
-----------
Letter grades and elifs


Directions:
----------
    - Accept a numeric grade from the user and display a letter grade. 
        The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
    - Check to see if the number given is between 0 and 100.  


Sample Output:
--------------
Enter the numeric grade: 85
The letter grade is: B




"""


#accept a numeric grade from the user and display a letter grade

numeric_grade = float(input("Enter your numeric grade: "))

# Check if the grade is between 0 and 100
if 0 <= numeric_grade <= 100:
    # Determine the letter grade based on the grading scale
    if numeric_grade >= 90:
        letter_grade = 'A'
    elif numeric_grade >= 80:
        letter_grade = 'B'
    elif numeric_grade >= 70:
        letter_grade = 'C'
    elif numeric_grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Display the letter grade
    print("Your letter grade is:", letter_grade)
else:
    print("Invalid grade. Grade must be between 0 and 100.")