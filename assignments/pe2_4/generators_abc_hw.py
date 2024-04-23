"""


Background:
-----------
Generators in Python are a powerful tool for creating iterators in a memory-efficient way. 
The yield statement is used to produce a sequence of values over time, pausing the function execution between each one.


Task:
-----
Create a Python program that uses a generator function to produce all possible two-letter combinations from a given list of characters.
 For example, if the list is ['a', 'b', 'c'], the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'.

 
Instructions:
-------------
1. Define a generator function two_letter_combinations that takes a list of characters as an argument.
2. Use nested loops within the generator function to iterate over the list of characters. 
    In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
3. In the main method, call the generator function with a list of characters and iterate over the generator to print each combination.
    Create an original  5-letter list.
4. Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
 

Example:
--------

def two_letter_combinations(characters):
    # Implement the generator function

def main():
    # Call the generator function and print each combination


main()

"""

# create generator to use in the main function
def two_letter_combinations(emojis):

    # goes through each emoji in a list
    for emoji1 in emojis:

        # goes through each emoji again
        for emoji2 in emojis:

            # takes the 2 "for's" above and adds them together
            yield emoji1 + emoji2


# make use of the generator above and put it all together
def main():

    # creating the characters
    emojis = ['🐥', '🐣', '🦆', '🐤', '🪿'] 

    #makes for better readability when finally printed        
    print("2 letter combinations:  ")

    #loop uses the generator with the characters above
    for combo in two_letter_combinations(emojis):

        #prints out all of the combos created
        print(combo)

main()