
def main():
    print("Welcome to the Konditorei.")
    print()

    amount = float(input("How many pounds of coffee do you want? "))
    coffeeCost = 10.5 * amount
    shipping = 0.86 * amount + 1.5 

    print() 
    print("Cost of coffee : ", coffeeCost)
    print("Shipping : " , shipping)
    print("-----------------------------------------------")
    print("Total due : ",coffeeCost + shipping)

main()


>>>>>>>>>>

Welcome to the Konditorei.

How many pounds of coffee do you want? 9.63

Cost of coffee :  101.11500000000001
Shipping :  9.7818
-----------------------------------------------
Total due :  110.89680000000001
Press any key to continue . . .
