"""

Assignment:
-----------
5 names from user
 

Accomplish the following tasks:
---------------
1. Accept five names from the user.
2. Store these names in a list.
3. Sort the list using the Bubble Sort algorithm. 
4. Finally, reverse the sorted list using a Python list method. 

Requirements:
-------------
- Your program should prompt the user to enter five names.
- Use a loop to accept each name and append it to a list.
- Implement the Bubble Sort algorithm to sort the list of names in ascending order.
- Print the sorted list.
- After sorting, use a Python list method to reverse the order of the list.
- Print the final reversed list to the console.


"""

# get five names
names = []

# ask until five names are given
for i in range(5):
    name = input("Enter name {}: ")
    names.append(name)

# bubble sort names
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i + 1], names[i]

# Print sorted list
print("Sorted names:", names)

# Reverse list
names.reverse()

# Print reversed list
print("Reversed sorted names:", names)