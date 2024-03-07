# create a tuple for classes

# make def
def main():
    programming_class = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    for classes in programming_class:
        print(classes, end = " ")

    print(f"\n{len(programming_class)} are the classes in programming.")

main()