"""

Assignment: ASCII Value Finder

Write a Python program to get a single character from the user and return its ASCII value.

Step-by-Step Instructions:
-------------------------
1. Start your Python script: Open your Python environment and start a new script. 
    - Make sure to use a main() function.
2. Prompt for User Input: 
    - Use the input() function to ask the user to enter a character.
        user_input = input("Enter a character: ")
3. Validate the Input: 
    - Implement a loop to ensure the input is only one character. 
    - Use the len() function to check the length of the input.
        while len(user_input) != 1:
            print("Please enter exactly one character.")
            user_input = input("Enter a character: ")
    - Explain that the loop will continue asking for input until the user enters exactly one character.
4. Convert to ASCII Value: Once a valid character is received, use the ord() function to convert the character to its ASCII value.
5. ascii_value = ord(user_input)
    - Display the Result: Print the ASCII value to the user.
    - print(f"The ASCII value of {user_input} is {ascii_value}")

"""

# create a program that gives ascii code 

# have user input character
user_input = input("Enter a character: ")

# create a loop to 
while len(user_input) != 1:
    print("Please enter exactly one character.")
    user_input = input("Enter a character: ")

# convert to the ascii value
ascii_value = ord(user_input)

# display the result
print(f"The ASCII value of {user_input} is {ascii_value}")