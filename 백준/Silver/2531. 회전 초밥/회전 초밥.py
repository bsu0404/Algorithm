N, d, k, c = map(int,input().split())

arr = list(map(int, (input() for _ in range(N))))
count = [0] * (d + 1)
numSet = set()
maxCount = 0


for i in range(N + k):
    num = arr[i % N]
    count[num] += 1
    numSet.add(num)

    if i >= k:
        num = arr[(i - k)%N]
        count[num] -= 1
        if count[num] == 0:
            numSet.remove(num)

    if c in numSet:
        dish = len(numSet)
    else:
        dish = len(numSet) + 1
    
    maxCount = max(maxCount, dish)
    


print(maxCount)