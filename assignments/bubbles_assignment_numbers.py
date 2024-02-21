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