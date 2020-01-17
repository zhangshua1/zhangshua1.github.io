def fib(max):
	n,a,b = 0,0,1
	while n < max:
		#print(b)
		yield b
		a,b = b, a+b
		#a = b 
		#b = a + b
		n = n + 1
	return '----done----'

print(fib(100))
f = fib(100)

for i in f:
	print(i)
