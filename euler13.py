def readData(filename):
	with open(filename) as file:
		numbers = file.readlines()

	return numbers

def calcSum(numbers):
	c = 0
	d = 0
	result = "";
	for i in range(49, -1, -1):
		d = 0
		for j in range(0, 100):
			d += int(numbers[j][i])

		result = str((d + c) % 10) + result
		c = (d + c) // 10

	result = str(c % 10) + result
	result = str(c // 10) + result
	return result

print(calcSum(readData('euler13.txt'))[:10])
