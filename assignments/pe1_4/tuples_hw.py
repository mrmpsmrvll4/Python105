"""

Assignment: Create and Use Tuples

Now, let's practice using tuples. Imagine you're planning the classes for a programming certificate.
     You need to list out six classes. Here's what you need to do:

1. Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python',
     'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.

2. Write a program that uses a for loop to print each class in the tuple.

3. Use the len function to print how many classes are in the tuple.

4. Make sure to use a main function for this program.

Try this out, and you'll get a good grasp of how tuples work in Python!


"""

# create a tuple for classes

# make def
def main():
    programming_class = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    for classes in programming_class:
        print(classes, end = " ")

    print(f"\n{len(programming_class)} are the classes in programming.")

main()