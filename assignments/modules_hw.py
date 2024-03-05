import random

# create a random number guessing game

def game(win):
    try:
        guess = int (input("Guess a number between 1 and 100:  "))

        # print value hot, etc.

        if:
            print()
        else:
            print("That is not a valid value")
            game(win)

    except:
        print()
        game(win)

def main():
    win = random.randint(1,100)
    print(win)
    game(win)