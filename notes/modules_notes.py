import random

# create a number guessing game program with 

def game(win):
    try:
        guess = int (input("Guess a number between 1 and 100:  "))
        # print value hot, etc.
        distance = abs(win - guess)
        if distance == 0:
            print("You win!")
        elif distance <= 5:
            print("Very hot")
        elif distance <= 15:
            print("Hot")
        elif distance <= 25:
            print("Cool")
        else:
            print("Cold")
        game(win)
    except:
        print("That is not a valid value")
        game(win)

def main():
    # test random
    win = random.randint(1,100)
    print(win)
    game(win)

main()