"""

Assignment: Personal Diary

Objective: Create a Python program that functions as a personal diary. Users should be able to add entries with the date and time they provide, which are then saved to a file.
----------
Detailed Directions
1. Set Up Your Python Environment: Create a diary folder for this assignment, you will upload the whole file to GitHub when you are done. 
2. Create a New Python File: Name this file personal_diary.py.
3. Writing the Code:
    - Create this in a main function
    - Prompt the user to enter the current date and time, then a diary entry.
    - Open or create a file named diary.txt in append mode using open().
    - Write the user-provided date, time, and diary entry into the file. 
      Ensure each entry is separated from the others by writing a blank line after entering the date/time line and the entry line. 
    - Close the file using the close() method.
4. Comments and Documentation: Add comments to your code explaining its functionality.
5. Testing the Program: Run personal_diary.py three times, each time entering a different diary entry along with the date and time. Check diary.txt to ensure entries are recorded correctly.
6. Submission: Submit both your personal_diary.py file and the diary.txt file containing your entries. 

"""
# open the file to start adding to it
def open_file():

    #set the try and except
    try:

        # Open the file in read mode
        directory = open('diary.txt', 'r')

        # we can read and write (append)
        content = directory.read()

        # print out what content exists
        print(content)

        # close the file
        directory.close()

        return (content)
    
    # create error if the file doesn't currently exist
    except FileNotFoundError:
        print("File not found.")

    # 
    except IOError:
        print("We created this file for you, it did not exist or was empty.")

    # create an error if some other error arises
    except Exception as e:
        print("An error occurred:", e)



# add to the diary
def add_values(my_values):
    # set input for the date, time and the entry
    date = input("What is the current date?:  ")
    time = input("What is the current time?:  ")
    entry = input("Please make an entry!:  ")

    #add the 3 inputs together together for readability
    entry = date + ", " + time + ", " + entry + "\n"


    # open the diary
    record = open('diary.txt', 'a')

    # write to the diary
    record.write(entry)

    # make sure to close diary
    record.close()

# def main to bring it all together
def main():
    values = open_file()
    print(f"The contents of the file are: {values}")
    add_values(values)


main()