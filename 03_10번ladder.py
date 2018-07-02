import math

def main():
    print("This program helps to determine the length of ladder needed")
    print("to reach a give height.") 
    print() 


    height = float(input("How high must you reach? "))
    angle = float(input("What will the ladder angle be (in degrees)?"))


    radians = math.pi * angle /180 
    length = height / math.sin(radians)

    print()
    print("Length of ladder required :", length)

main()


>>>>>>>>>>>>

This program helps to determine the length of ladder needed
to reach a give height.

How high must you reach? 9.9
What will the ladder angle be (in degrees)?6

Length of ladder required : 94.71104511170572
Press any key to continue . . .
