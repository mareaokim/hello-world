#P.52 프로그래밍 과제
def main():
    print("섭씨온도를 화씨온도로 변환하는 프로그램 입니다.")

    celsius = eval(input("what is the celsius temperature?"))
    fahrenheit = 9/5*celsius+32
    print("The temperature is", fahrenheit, "dgrees Fahrenheit.")
    
main()
