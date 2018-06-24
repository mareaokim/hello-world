def main():
    print("This program calculates the future value of a yearly investment")
    print()


    pay=eval(input("Enter amount to invest each year : "))
    apr = eval(input("Enter the annual interest rate : ")) 
    years = eval(input("Enter the number of years: "))

   
    principal = 0.0

    for i in range(years):
        principal = (principal + pay) * (1+apr)

        
    print("The amount in", years, "years is:" , principal)

        
main()


>>

This program calculates the future value of a yearly investment

Enter amount to invest each year : 6
Enter the annual interest rate : 2
Enter the number of years: 1
The amount in 1 years is: 18.0
Press any key to continue . . .
