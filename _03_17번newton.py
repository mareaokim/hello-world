import math

def main():
    print("This is program calculates square root using Newton's method.")
    print()

    x = float(input("Enter number to find the root of:"))
    n = int(input("How many iterations should i use?"))


    guess = x / 2.0
    for i in range(n):
        guess = (guess + x/guess)/2.0

        print()
        print("Approximate square root:",guess)
        print("Difference from math.sqrt:",math.sqrt(x) - guess)

main()

