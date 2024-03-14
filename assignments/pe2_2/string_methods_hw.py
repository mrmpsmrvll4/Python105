# use string methods


def main():

    # capitalize the first letter
    string1 = "python"
    print(string1.capitalize())
    

    # center the string
    string2 = "python"
    print(string2.center(10, '*'))


    # check if string ends with specific substring
    string3 = "python"
    print(string3.endswith("on"))


    # check for first occurance of substring
    string4 = "python"
    print(string4.find("th"))


    # check if all characters are alphanumeric
    string5 = "python3"
    print(string5.isalnum())


    # check if all characters are alphabetic
    string6 = "python"
    print(string6.isalpha())

    
    # check if all characters are lowercase
    string7 = "python"
    print(string7.islower())


    # check for white spaces
    string8 = "   "
    print(string8.isspace())


    # check if all are uppercase
    string9 = "PYTHON"
    print(string9.isupper())


    # join elements of an iterable with the string as the separator
    iterable1 =  ["Python", "is", "fun"]
    separator = "-"
    print("-".join(["Python", "is", "fun"]))


    # make letters to lowercase
    string10 = "PYTHON"
    print(string10.lower())
    

    # remove leading characters (spaces)
    string11 = "  python"
    print(string11.lstrip())


    # remove trailing chacters (spaces)
    string12 = "python  "
    print(string12.rstrip())


    # replace all occurrences of a substring with another substring
    string13 = "I love python"
    print(string13.replace("python", "snake"))


    # find the highest index of a substring
    string14 = "python"
    print(string14.rfind("n"))


    # split the string at a specified separator
    string15 = "python-is-fun"
    print(string15.split())


    # check if the string starts with a specified substring
    string16 = "python"
    print(string16.startswith("py"))


    # remove both leading and trailing characters (spaces by default)
    string17 = "  python  "
    print(string17.strip())


    # swap the case of all characters in the string
    string18 = "Python"
    print(string18.swapcase())


    # convert the first character of each word to uppercase
    string19 = "python is fun"
    print(string19.title())


    # convert all characters in the string to uppercase
    string20 = "python"
    print(string20.upper())


main()