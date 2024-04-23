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