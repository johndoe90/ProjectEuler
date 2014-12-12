cache = {}

def latticePaths(x, y):
    if x == 0 or y == 0:
        return 1

    key = (x,y)
    if key in cache:
        return cache[key]

    result = latticePaths(x-1, y) + latticePaths(x, y-1)
    cache[key] = result
    return result

print(latticePaths(20,20))
