import sys
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0

def findGood(k):
    goal = arr[k]
    global cnt
    i = 0
    j = len(arr)-1
    while i < j :
        value = arr[i] + arr[j]
        if k == i :
            i += 1
            continue
        elif k == j:
            j -= 1
            continue
        if value == goal:
            cnt += 1
            break
        elif arr[i] + arr[j] < goal:
            i+=1
        elif arr[i] + arr[j] > goal:
            j-=1

for i in range(N):
    findGood(i)
print(cnt)