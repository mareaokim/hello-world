def main():
    print("average")
    print()

    n = int(input("How many numbers do you have?"))
    total = 0
    for i in range(n):
        num = float(input("Enter a number: "))
        total = total + num

        print()
        print("The average of the numbers is:", total/n)

main()

>>>>>>>>>>>>>>>>>>>>>>

average

How many numbers do you have? 8
Enter a number: 66

The average of the numbers is: 8.25
Enter a number: 9

The average of the numbers is: 9.375
Enter a number: 44

The average of the numbers is: 14.875
Enter a number:

