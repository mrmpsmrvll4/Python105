"""

Assignment: NATO Phonetic Alphabet Dictionary

Objective:
Your mission is to create a Python program that uses a dictionary to translate letters into the
 NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.

I would plan this program before attempting it. Here is what pseudocode would look like for this program:


 code to start with:
-------------------

Start

 Step 1: Create the NATO Phonetic Alphabet Dictionary
    Define nato_alphabet as a dictionary with each English alphabet letter as a key and its NATO phonetic term as the value
    Example: {"A": "Alpha", "B": "Bravo", ..., "Z": "Zulu"}

 Step 2: Develop the Spelling Program
    Define a function spell_word():
        Prompt user for a word and store it in a variable 'user_word'
        Convert 'user_word' to uppercase (to match dictionary keys)

        For each letter in 'user_word':
            Find the corresponding NATO phonetic term in nato_alphabet
            Print the NATO phonetic term

 Step 3: Incorporate a Main Function
    Define main():
        Call the spell_word() function

 Step 4: Test Your Program
    Call main()

End


Steps to Follow:
---------------
1. Create the NATO Phonetic Alphabet Dictionary:
    - Begin by constructing a dictionary in Python named nato_alphabet.
    - Each key in this dictionary should be a letter of the English alphabet, and its corresponding value should be the NATO phonetic term. For example, {"A": "Alpha", "B": "Bravo", ...}.
    - Here's a snippet of the NATO Phonetic Alphabet for reference:
        A - Alpha
        B - Bravo
        C - Charlie
        ...
        Z - Zulu

2. Develop the Spelling Program:
    - Write a function that prompts the user to input a word.
    - The program should then iterate through each letter of the input word.
    - For each letter, find the corresponding NATO phonetic term in your dictionary and print it out.
    - Ensure your program can handle both uppercase and lowercase inputs.

3. Incorporate a Main Function:
    - Encapsulate your program logic within a main() function.
    - This is a best practice in Python programming, making your code organized and more readable.

4. Test Your Program:
    - After completing your program, test it with various words to ensure it works correctly.
    - Try both common and unusual words to thoroughly test the functionality.

Example Output:
---------------
    - If the user inputs the word "Hello", your program should output:

        Hotel
        Echo
        Lima
        Lima
        Oscar

"""

# create a program using dictionaries 


def main():
    nato_alphabet={"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta",
               "e":"echo", "f":"foxtrot", "g":"golf", "h":"hotel", "i":"india,", 
               "j":"juliette", "k":"kilo", "l":"lima", "m":"mike", "n":"november", 
               "o":"oscar", "p":"papa", "q":"quebec", "r":"romeo", "s":"sierra", "t":"tango", 
               "u":"uniform", "v":"victor", "w":"whiskey", "x":"xray", "y":"yankee", "z":"zulu", " ":" "}

    word = input("Enter word: ")
    # takes the word from user and makes it lowercase
    for letter in word.lower():
        converted_letter = nato_alphabet[letter]
        print(converted_letter)

    

main()