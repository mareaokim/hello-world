Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program illustrates a chaotic function")
	x=eval(input("Enter a number between 0 and 1 : "))
	for  i  in range(10):
		x= 3.9 * x * (1-x)
		print(x)
		 y=eval(input("Enter a number between 0 and 1 : "))
		 
SyntaxError: unexpected indent
>>> def main():
	print("This program illustrates a chaotic function")
	x=eval(input("Enter a number between 0 and 1 : "))
	for  i  in range(10):
		x= 3.9 * x * (1-x)
		print(x)
	y=eval(input("Enter a number between 0 and 1 : "))
	for i in range(10):
		y=3.9 * y *(1-y)
		print(y)

		
>>> main()
This program illustrates a chaotic function
Enter a number between 0 and 1 : .25
0.73125
0.76644140625
0.6981350104385375
0.8218958187902304
0.5708940191969317
0.9553987483642099
0.166186721954413
0.5404179120617926
0.9686289302998042
0.11850901017563877
Enter a number between 0 and 1 : .26
0.75036
0.73054749456
0.7677066257332165
0.6954993339002887
0.8259420407337192
0.5606709657211202
0.9606442322820199
0.14744687593470315
0.49025454937601765
0.9746296021493285
>>> 
