
#문제 2
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1 : "))
    input("Press the <Enter> key to quit.")
    for i in range(10):
        x = 3.9 * x *(1-x)
        print(x)
main()
