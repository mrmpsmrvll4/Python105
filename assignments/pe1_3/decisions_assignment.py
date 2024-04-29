"""

Assignment:
-----------
decisions using age limits
 

Write a Python program that uses if else statements and:
---------------------
    - Ask the user for their age.
    - Check to see if the user is old enough to drive.
    - Check to see if the user can vote.
    - Check to see if the user can legally buy alcohol.
    - Check to see if the user is eligible for a senior discount (65).
    - Print all the results on the screen.


Sample Result:
--------------
How old are you? 52
You are old enough to drive.
You can vote.
You can buy alcohol legally.
You are not eligible for the senior discount.


"""

#What is your age and how does it affect you with laws?

age = input("How old are you?")

#check if age is 16 or older
if age >= "16":
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")

#check if age is 18 or older
if age >= "18":
    print("You can vote")
else:
    print("You cannot vote")

#check if age is 21 or older
if age >= "21":
    print("You can buy alcohol legally")
else:
    print("You cannot buy alcohol legally")

#check if age is less than 65
if age < "65":
    print("You are not eligible for a senior discount")
else:
    print("You are eligible for a senior discount")