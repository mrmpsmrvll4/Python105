"""

Assignment: Number Guessing Game

In this assignment, you will create a Python program that generates a random number between 1 and 100. 
Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.

Assignment Objectives:
---------------------
- Use the random module to generate a random number.
- Implement a while loop to allow continuous guessing until the correct number is guessed.
- Use the abs() function to determine the difference between the guess and the actual number.
- Provide feedback based on the proximity of the guess to the actual number.

Task Details:
------------
1. Import the random module and use it to generate a random number between 1 and 100.
2. Put the rest of the code in the main function; use try and except statements. The except statement should look for ValueError
3. Write a while loop that allows the user to enter a guess for the number.
4. Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
5. Based on this difference, provide the following feedback to the user:
    - If the difference is within 5, print "Very Hot".
    - If the difference is within 15, print "Hot".
    - If the difference is within 25, print "Cool".
    - If the difference is more than 25, print "Cold".
6. The loop should continue until the user guesses the correct number.
7. Make sure to call the main function!

Additional Notes:
----------------
The abs() function is a built-in Python function used to calculate the absolute value of a number. 
The absolute value of a number is its distance from zero on the number line, regardless of direction. 
For example, abs(-5) and abs(5) both return 5.

"""

import random

# create a number guessing game program with 

def game(win):
    try:
        guess = int (input("Guess a number between 1 and 100:  "))
        # print value hot, etc.
        distance = abs(win - guess)
        if distance == 0:
            print("You win!")
        elif distance <= 5:
            print("Very hot")
        elif distance <= 15:
            print("Hot")
        elif distance <= 25:
            print("Cool")
        else:
            print("Cold")
        game(win)
    except:
        print("That is not a valid value")
        game(win)

def main():
    # test random
    win = random.randint(1,100)
    print(win)
    game(win)

main()