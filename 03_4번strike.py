def main():
    print("This program calculates the distance from a lightning strike.")
    print()


    seconds = int(input("Enter number of seconds between flash and crush : "))
    feet = 1100 * seconds
    miles = feet / 5280.0

    print() 
    print("The lightning is approximately" , round(miles,1) , "miles away.")

main()


>>>

This program calculates the distance from a lightning strike.

Enter number of seconds between flash and crush : 6900

The lightning is approximately 1437.5 miles away.
Press any key to continue . . .
