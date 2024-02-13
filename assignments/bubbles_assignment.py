def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Accept five names from the user
names = []
for i in range(5):
    name = input("Enter name {}: ".format(i + 1))
    names.append(name)

# Sort the list using the Bubble Sort algorithm
bubble_sort(names)

# Print the sorted list
print("Sorted names:", names)

# Reverse the sorted list using a Python list method
names.reverse()

# Print the final reversed list
print("Reversed sorted names:", names)