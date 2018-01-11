def fib (n):
	if n < 2:
		return n
	return fib(n-2)+fib(n-1)


n = int(input("Enter the number of times you want to input n :"))
for i in range (0,n):
	a = int(input ("Enter number :"))
	print (fib(a))