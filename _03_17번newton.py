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

>>>>>>>>>>>>>>>>>>
This is program calculates square root using Newton's method.

Enter number to find the root of:98
How many iterations should i use?5

Approximate square root: 25.5
Difference from math.sqrt: -15.600505063388335

Approximate square root: 14.67156862745098
Difference from math.sqrt: -4.772073690839315

Approximate square root: 10.675577163708784
Difference from math.sqrt: -0.7760822270971186

Approximate square root: 9.927704353956496
Difference from math.sqrt: -0.028209417344831067

Approximate square root: 9.899535014921744
Difference from math.sqrt: -4.00783100786839e-05
Press any key to continue . . .
