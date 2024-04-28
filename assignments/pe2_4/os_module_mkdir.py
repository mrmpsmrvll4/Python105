'''

Assignment: Basic File Operations Script

In this assignment, you will create a Python script to practice basic file operations using the os module. 
Your script will organize files into newly created directories based on their file types.

Objectives
----------
- Create a new directory.
- Create subdirectories and organize files into them.
- Understand and apply basic file operations in Python.
 

Instructions
------------
1. Create a new Python script named file_organizer.py.
2. Use the os.mkdir() function to create a new directory named MyFiles.
3. Inside MyFiles, create three subdirectories named Docs, Images, and Videos using the same mkdir() function.

'''


# cars
import os

def main():
    # create a vehicle folder
    os.mkdir("cars")
    os.mkdir("cars/sedans")
    os.mkdir("cars/sedans/prius")
    os.mkdir("cars/coupes")
    os.mkdir("cars/coupes/mustang")
    os.mkdir("cars/not_cars")
    os.mkdir("cars/not_cars/trucks")

main()