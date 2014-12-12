cache = {}

def digitSum(n):
	sum = 0
	while n > 0:
		sum += n % 10
		n //= 10
	
	return sum

def factorial(n):
	if n in cache:
		return cache[n]

	if n == 1:
		return 1

	cache[n] = n * factorial(n-1)
	return cache[n]

print(digitSum(factorial(100)))
