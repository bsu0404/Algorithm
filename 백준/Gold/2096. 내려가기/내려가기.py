import sys

MOVE = [[1,0],[1,-1],[1,1]]      

N = int(input())
arr = list(map(int,input().split()))
maxDp, minDp = arr, arr

for i in range(1, N):
    nextMax, nextMin =[0, 0, 0],[sys.maxsize, sys.maxsize, sys.maxsize]
    arr = list(map(int,input().split()))

    for j in range(3):
        for k in range(-1,2):
            if 0 <= j + k <= 2:
                nextMin[j] = min(minDp[j+k] + arr[j] , nextMin[j])
                nextMax[j] = max(maxDp[j+k] + arr[j] , nextMax[j])
    maxDp, minDp = nextMax, nextMin


print(max(maxDp), min(minDp))