"""
Set up your program in a main() function
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
"""


def main():
    valid = False  # change to true if all condions are met
    while not valid:
        print("""Password Requirements:\n
            Between 8 to 20 characters long.\n
            Contains at least one uppercase letter.\n
            Contains at least one lowercase letter.\n
            Includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*\n""")

        password = input("Please enter a password that meets the criteria: ")
        length = len(password)

        if length < 21 and length > 7:
            valid = True
        else:
            valid = False


            # check if password has a capital

        for letter in password:

            if letter.isupper():
                valid = True

            else:
                valid = False 


        #check if letter has lowercase
                
        for letter in password:

            if letter.islower():
                valid = True
            else:
                valid = False


        # check if password has a number
                
        for letter in password:
            
            if letter.isnumeric():
                valid = True
            else:
                valid = False


        # check if password has a symbol

        has_symbol = False
        symbol = ['!', '@', '#']
       
        for letter in password:

            if letter in symbol:
                has_symbol = True
                valid = True
                
            else:
                valid = False

        
        # 
                
        if valid:
            print("You have successfully created a password!")
        else:
            print("That password is not the right length")
            print("That password does not have a capital")
            print("That password does not have a lower case")
            print("That password does not have a number")
            print("you need to include a symbol")
            continue

main()
