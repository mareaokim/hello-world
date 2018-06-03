Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program illustrates a chaotic function")
	x=eval(input("Enter a number between 0 and 1 : "))
	n=eval(input("How many numbers should I print?"))
	for  i  in range(n):
		x= 3.9 * x * (1-x)
		print(x)

		
>>> main()
This program illustrates a chaotic function
Enter a number between 0 and 1 : .25
How many numbers should I print?5
0.73125
0.76644140625
0.6981350104385375
0.8218958187902304
0.5708940191969317
>>> 
