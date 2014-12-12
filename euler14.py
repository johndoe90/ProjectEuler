cache = {}

def collatzLength(num):
    if num in cache:
        return cache[num]

    if num == 1: 
        return 1
    
    result = 0
    if num % 2 == 0:
        result = 1 + collatzLength(num // 2)
    else:
        result = 1 + collatzLength(3 * num + 1)

    cache[num] = result
    return result

def findLongestCollatz():
    longest = (0,0) 
    for i in range(1, 1000000):
        length = collatzLength(i)
        if length > longest[1]:
            longest = (i,length)

    return longest

print(findLongestCollatz())
