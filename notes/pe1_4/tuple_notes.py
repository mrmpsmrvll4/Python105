#create a tuple

def main():
    months = ("January", "February", "March", "April", "May", "June", "July", "Augst", "September", "October", "November", "December" )

    for month in months:
        print(month, end = " ")

    print(f"\nThere are : {len(months)} months in a year")

    summer.append(months[4:7])
    print("Summer includes: ")
    for month in summer:
        print(month, end = "  ")
    print("\n\n")
    summer.append("August")
    print(summer)

main()