def triangularNumberGenerator():
	t = 0
	n = 0
	while True:
		n += 1
		t += n
		yield t

def numOfDivisors(n):
	divisors = 0
	left = 1
	right = n

	while left < right:
		if n % left == 0:
			divisors += 2
			right = n // left

		left += 1

	return divisors

generator = triangularNumberGenerator()

cond = True
while cond:
	n = next(generator)
	cond = numOfDivisors(n) <= 500 

print(n)

