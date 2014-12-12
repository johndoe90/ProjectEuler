def fib():
	yield 1
	yield 1

	a = 1
	b = 1
	while True:
		c = a + b
		a = b
		b = c

		yield c

n = 0
gen = fib()
cond = True
while cond:
	cond = len(str(next(gen))) < 1000
	n += 1

print(n)
