cache = {}

def divisorsOf(n):
	if n in cache: return cache[n]

	divisors = []
	for i in range(1, n // 2 + 1):
		if n % i == 0:
			divisors.append(i)

	cache[n] = divisors
	return divisors

def amicableNumbers():
	result = 0
	for i in range(1, 10000):
		dA = sum(divisorsOf(i));
		dB = sum(divisorsOf(dA));

		if i != dA and i == dB:
			result += i

	return result

print(amicableNumbers())

