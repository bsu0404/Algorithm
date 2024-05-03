# function

def swap(i, j, num):
    tmp = num[i]
    num[i] = num[j]
    num[j] = tmp
    return num

def bfs(num, count):

    global maxNum, swapCount
    number = int("".join(num))
    numSet.add((number, count))

    if count == 0:
        n = int("".join(num))
        maxNum = max(maxNum, n)
        swapCount += 1
        return 
    
    for i in range(len(N)):
        for j in range(len(N)):
            if i != j:
                n = swap(i, j, num[:])
                number = int("".join(n))

                if n[0] != "0" and (number,count-1) not in numSet:
                    bfs(n, count - 1)
# main

import sys
sys.setrecursionlimit(10 ** 6)

N, cnt = input().split()
cnt = int(cnt)
N = list(N)
numSet = set()

maxNum = 0
swapCount = 0

bfs(N, cnt)

if swapCount == 0:
    print(-1)
else:
    print(maxNum)
