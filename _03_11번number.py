def main():
    print("natural numbers.")
    print()

    n = int(input("Please enter a value for n : "))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

        print()
        print("The sum from 1 to",n,"is:",sum )

main()