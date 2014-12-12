cache = {}

def factorial(n):
    if n in cache:
        return cache[n]

    if n == 1:
        return 1

    if n == 0:
        return 1

    cache[n] = n * factorial(n-1)
    return cache[n]

def digitFactorials():
    result = 0
    for i in range(3, 2540161):
        sum = 0
        num = i
        while num > 0:
            d = num % 10
            num //= 10
            sum += factorial(d)

        if sum == i:
            result += i

    return result

print(digitFactorials())
