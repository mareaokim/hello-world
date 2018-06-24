def main():
    print("This program calculates the future value")
    print()


    principal = eval(input("Enter the initial principal : "))
    
    rate = eval(input("Enter the annual interest rate: ")) 

    periods = eval(input("Enter the number of compounding periods per year:"))
    
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1+rate/periods)

        print("The amount in", years, "years is:" , principal)

        
main()

>>>>

This program calculates the future value

Enter the initial principal : 5
Enter the annual interest rate: 2
Enter the number of compounding periods per year:6
Enter the number of years: 1
The amount in 1 years is: 6.666666666666666
The amount in 1 years is: 8.888888888888888
The amount in 1 years is: 11.85185185185185
The amount in 1 years is: 15.802469135802465
The amount in 1 years is: 21.06995884773662
The amount in 1 years is: 28.093278463648822
Press any key to continue . . .
