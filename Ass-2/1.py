#Python Program to check Armstrong Number
n = 153
a = n
b = len(str(n))
x = 0
while n != 0:
	r = n % 10
	x = x+(r**b)
	n = n//10
if a == x:
	print(a)
else:
	print(a)