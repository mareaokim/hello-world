Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> def main():
	print("This program illustrates a chaotic function")
	x=eval(input("Enter a number between 0 and 1 : "))
	for  i  in range(20):
		x= 3.9 * x * (1-x)
		print(x)

		
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
0.4074120362630336
0.9415671289870646
0.214572035332672
0.6572704202448796
0.8785374581723959
0.4161666317654883
0.9475906688447814
0.19368411333601687
0.6090652525513056
0.9286086056750876
>>> 
>>> def main():
	print("This program illustrates a chaotic function")
	x=eval(input("Enter a number between 0 and 1 : "))
	for  i  in range(20):
		x= 3.9 * x * (1-x)
		print(x)

		
>>> main()
This program illustrates a chaotic function
Enter a number between 0 and 1 : 6.9
-158.769
-98928.82100790001
-38169341163.853096
-5.681904559191041e+21
-1.2590775373704814e+44
-6.182577355932573e+88
-1.490746247721518e+178
-inf
-inf
-inf
-inf
-inf
-inf
-inf
-inf
-inf
-inf
-inf
-inf
-inf
>>> 
