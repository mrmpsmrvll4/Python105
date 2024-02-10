#ask the user for two integer inputs
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#and
print("Both numbers greater than 5:", num1 >5 and num2 > 5)
print("Both numbers greater than 50:", num1 > 50 and num2 > 50)

#or
print("Either number is odd?", num1 % 2 != 0 or num2 % 2 != 0)
print("Either number is less than 50?", num1 < 50 or num2 < 50)

#not
print("num2 is not equal to num1:", num2 != num1)
print("num1 is not 5:", not num1 == 5)