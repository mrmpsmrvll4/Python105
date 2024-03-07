# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

    except ValueError:
        print("That is not a number. Please enter a number.")

    else:
        print("Thank you for using the square program.")
    
    finally:
        print("Program ended")

square_number()