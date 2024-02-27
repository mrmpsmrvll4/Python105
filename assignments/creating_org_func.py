#Calculating Factorials

def factorial(base):
    if base >= 1:
        return base
    elif base > 1:
        return base * factorial(base - 1)


def main():
    base = int(input("Enter the number: "))
    total_amount = factorial
    print(f"The factorial of {base} is:  ")


main()