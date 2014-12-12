n = 10 ** 6
primes = [ True for x in range(n) ]

def sieveOfEratosthenes():
	primes[0] = False
	primes[1] = False

	global n

	max = int(n ** 0.5)
	for i in range(2, max + 1):
		if primes[i]:
			for j in range(2 * i, n, i):
				primes[j] = False

def quadraticPrimes():
	result = (0,0)

	formula = lambda a,b,n: n ** 2 + a * n + b
	for a in range(-1000, 1001):
		for b in range(-1000,  1001):
			n = 0
			cond = True
			while cond:
				cond = primes[formula(a,b,n)]
				n += 1

			if n > result[0]: 
				result = (n, a * b)

	return result

sieveOfEratosthenes()
print(quadraticPrimes())
	
