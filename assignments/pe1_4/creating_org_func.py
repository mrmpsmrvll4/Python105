#Calculating Factorials

def factorial(base):
    if base == 1:
        return base
    elif base > 1:
        return base * factorial(base - 1)

# set main def

def main():
    base = int(input("Enter the number: "))
    total_amount = factorial(base)
    print(f"The factorial of {base} is: {total_amount} ")


main()