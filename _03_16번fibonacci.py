def main():
    print("Fibonacci value")
    print()

    n = int(input("Enter the value of n:"))
    curr , prev = 1,1
    for i in range(n-2):
        curr,prev = curr + prev,curr

        print()
        print("The nth Fibonacci number is",curr)

main()

>>>>>>>>>>

Fibonacci value

Enter the value of n:8

The nth Fibonacci number is 2

The nth Fibonacci number is 3

The nth Fibonacci number is 5

The nth Fibonacci number is 8

The nth Fibonacci number is 13

The nth Fibonacci number is 21
Press any key to continue . . .


