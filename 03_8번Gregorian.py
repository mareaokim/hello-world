def main(): 
    print("Gregorian epact value of year.")
    print()

    year = int(input("Enter the year (e.g. 2020) : "))
    c = year // 100
    epact = (8+(c//4) - c + ((8*c+13)//25) + 11 * (year % 19)) %  30
    
    print()
    print("The epact value is" , epact, "days.")

main()


>>>>>>>>>>>>>>>

Gregorian epact value of year.

Enter the year (e.g. 2020) : 2030

The epact value is 25 days.
Press any key to continue . . .
