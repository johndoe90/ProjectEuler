import itertools

def spiralGen(l):
	yield 1

	n = 1
	level = 1
	while n < l ** 2:
		for i in range(4):
			n += 2 * level
			yield n

		level += 1

gen = spiralGen(1001)
print(sum(list(gen)))
