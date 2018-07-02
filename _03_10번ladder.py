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


