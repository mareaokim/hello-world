def main():
    print("allows you to total up some numbers")
    print()

    n = int(input("How many numbers do you have? : "))
    total = 0
    for i in range(n):
        num = float(input("Enter a number:"))
        total = total + num

        print()
        print("The sum of the numbers is:" , total)

main()

>>>>>

allows you to total up some numbers

How many numbers do you have? : 98
Enter a number:5

The sum of the numbers is: 5.0
Enter a number:
