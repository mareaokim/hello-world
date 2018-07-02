
def main():
    print("This program calculates the molecular weight of a hydrocarbon.") 
    print()

    h = int(input("Enter the number of hydrogen atoms : "))
    c = int(input("Enter the number of carbon atoms : "))
    ox = int(input("Enter the number of oxygen atoms : "))
    weight = 1.00794 * h + 12.0107 * c + 15.9994 * ox


    print()
    print("The molecular weight is :" , weight)

main()



>>>

This program calculates the molecular weight of a hydrocarbon.

Enter the number of hydrogen atoms : 45
Enter the number of carbon atoms : 56
Enter the number of oxygen atoms : 55

The molecular weight is : 1597.9234999999999
Press any key to continue . . .

