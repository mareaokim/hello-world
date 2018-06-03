Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number berween 0 and 1: "))
	for i  in range(10) :
		x = 2.0 * x * (1 - x)
		print(x)

		
>>> main()
This program illustrates a chaotic function
Enter a number berween 0 and 1: 6.9
-81.42000000000002
-13421.272800000006
-360287969.68964
-2.5961484292674182e+17
-1.3479973333575367e+35
-3.6341936214780595e+70
-2.6414726556783626e+141
-1.3954755581393002e+283
-inf
-inf
>>> def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number berween 0 and 1: "))
	for i  in range(10) :
		x = 2.0 * x * (1 - x)
		print(x)

		
>>> main()
This program illustrates a chaotic function
Enter a number berween 0 and 1: .25
0.375
0.46875
0.498046875
0.49999237060546875
0.4999999998835847
0.5
0.5
0.5
0.5
0.5
>>> 
