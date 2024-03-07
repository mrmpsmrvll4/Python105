# create a program using dictionaries 


def main():
    nato_alphabet={"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta",
               "e":"echo", "f":"foxtrot", "g":"golf", "h":"hotel", "i":"india,", 
               "j":"juliette", "k":"kilo", "l":"lima", "m":"mike", "n":"november", 
               "o":"oscar", "p":"papa", "q":"quebec", "r":"romeo", "s":"sierra", "t":"tango", 
               "u":"uniform", "v":"victor", "w":"whiskey", "x":"xray", "y":"yankee", "z":"zulu", " ":" "}

    word = input("Enter word: ")
    # takes the word from user and makes it lowercase
    for letter in word.lower():
        converted_letter = nato_alphabet[letter]
        print(converted_letter)

    

main()