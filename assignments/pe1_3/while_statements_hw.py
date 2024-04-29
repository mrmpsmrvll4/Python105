"""

Assignment
----------
For loops & 99 bottles of beer
 

Write the program "99 Bottles of Beer on the Wall" using a while loop. Be mindful to change the word 'bottles' to 'bottle' when you are down to the last one. 
You need to do the full 99 bottles the sample shows the last 3 verses.

Partial sample results - you need to do all 99 stanzas!:
----------------------

    3 bottles of beer on the wall
    3 bottles of beer
    Take one down, pass it around
    2 bottles of beer on the wall!

    2 bottles of beer on the wall
    2 bottles of beer
    Take one down, pass it around
    1 bottle of beer on the wall!

    1 bottle of beer on the wall
    1 bottle of beer
    take it down, pass it around
    No bottles of beer on the wall!

"""

def sing_99_bottles():
    bottles = 99

    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        elif bottles == 2:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        
        bottles -= 1

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

sing_99_bottles()