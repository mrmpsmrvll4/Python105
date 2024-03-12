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