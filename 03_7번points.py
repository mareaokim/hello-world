import math

def main():
    print("This program calculates the distance between two points.")
    print() 

    x1 = float(input("Enter the x for the first points : "))
    y1 = float(input("Enter the y for the first points : "))
    print()

    x2 = float(input("Enter the x for the second points : "))
    y2 = float(input("Enter the y for the second points : "))

    distance = math.sqrt((x2 - x1) **2 + (y2 - y1) ** 2)

    print()
    print("The distance between the points is" , distance)

main() 

>>>>>>>>

This program calculates the distance between two points.

Enter the x for the first points : 9
Enter the y for the first points : 5.6

Enter the x for the second points : 222.3
Enter the y for the second points : 36

The distance between the points is 215.4554478308683
Press any key to continue . . .

