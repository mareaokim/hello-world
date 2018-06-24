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
