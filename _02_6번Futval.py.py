
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