nums = set()

for i in range(1,10000):
    nums.add(i)

for i in range(1,10000):
    sumOfNum = i
    for j in str(i):
        sumOfNum += int(j)
    
    if sumOfNum in nums:
        nums.remove(sumOfNum)

print(*nums, sep="\n")
    