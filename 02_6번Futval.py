
def main():
    print("This program calculates the future value")
    print()


    principal = eval(input("Enter the initial principal : "))
    apr = eval(input("Enter the annual interest rate: ")) 
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1+apr)

        print("The amount in", years, "years is:" , principal)

        
main()




>>>>>

This program calculates the future value

Enter the initial principal : 6900
Enter the annual interest rate: 0.69
Enter the number of years: 1
The amount in 1 years is: 11661.0
Press any key to continue . . .
