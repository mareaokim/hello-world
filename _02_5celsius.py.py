def main():
	celsius = eval(input("What is the Celsius temperature? :"))
	for a in range(11):
		fahrenheit = 9/5 * celsius +32
		print(celsius, "Celsius temperature is", fahrenheit, "degrees Fahrenheit.")
		celsius = celsius + 10


main()
