max = 0

def readFile():
    with open("euler18.txt", "r") as file:
        nums = file.readlines()

    return list(map(lambda x: int(x), nums))

def findSum(nums, sum, i, level):
    global max

    if i >= len(nums):
        if sum > max: max = sum
    else:
        left = i + level
        right = i + level + 1
        findSum(nums, sum + nums[i], left, level + 1)
        findSum(nums, sum + nums[i], right, level + 1)

nums = readFile()
findSum(nums, 0, 0, 1)

print(max)
