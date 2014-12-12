def digitSum():
	sum = 0
	power = 2 ** 1000
	while power > 0:
		sum += power % 10
		power //= 10

	return sum

print(digitSum())
