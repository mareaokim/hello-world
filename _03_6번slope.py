
def main():
    print("The program calculates the slope of a line.")
    print()

    x1 = float(input("Enter the x for the first point : "))
    y1 = float(input("Enter the y for the first point : "))
    print()
    x2 = float(input("Enter the x for the second point : "))
    y2 = float(input("Enter the y for the second point : ")) 

    slope = (y2 - y1) / (x2 - x1)

    print()
    print("The slope of the line is" , slope)

main()
