"""

Assignment: Your own Madlib

Objective:
----------
Develop a Python-based Madlib based on a song of your choice. 
The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. 
The goal is to practice using functions, user input, and string manipulation in Python.

Important Note:
---------------
Choose any song you like for your madlib, but remember, no Rickrolling! 
Be creative and respectful in your song choice.

Task:
-----
1. Select a Song: Choose a song that is well-known and suitable for a classroom setting. 
    Avoid any song with inappropriate or offensive content.

2. Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. 
    These could include names, adjectives, nouns, places, etc.

3. Write the Function:
    - Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
    - Use f-strings to incorporate these parameters into the song's lyrics.
    - Ensure the function prints the customized song lyrics.

4. Collect User Input:
    - Write code to collect user input for each of the 8 variables.
    - Use clear and descriptive prompts to guide the user.

5. Call the Function:
    - Call the custom_song function with the user inputs as named arguments.
    - Ensure the order of arguments matches the parameters in your function definition


"""

# make a madlib of my own choosing please

# set the definition
def madlibs(adjective1, verb1, adjective2, noun1, verb2, adjective3, noun2, adjective4, adjective5):
    # my adlibs
    print(f"Our School cafeteria has really {adjective1} food.")
    print(f"Just thinking about it makes my stomach {verb1}.")
    print(f"The spaghetti is {adjective2} and tastes like {noun1}.")
    print(f"One day, I swear one of my meatballs started to {verb2}!")
    print(f"The turkey tacos are totally {adjective3} and look like old {noun2}.")
    print(f"My friend likes meatloaf, even though it's {adjective4} and {adjective5}")


# describe the variables
adjective1 = input("Please input an adjective:  ")
verb1 = input("Please input a verb:  ")
adjective2 = input("Please input an adjective:  ")
noun1 = input("Please input a noun:  ")
verb2 = input("Please input a verb:  ")
adjective3 = input("Please input an adjective:  ")
noun2 = input("Please input a noun:  ")
adjective4 = input("Please input an adjective:  ")
adjective5 = input("Please input an adjective:  ")


# make the output
madlibs(adjective1, verb1, adjective2, noun1, verb2, adjective3, noun2, adjective4, adjective5)
