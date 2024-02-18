import sys
N = int(input())

arr = list(map(int,input().split()))

arr.sort()
minValue = sys.maxsize
i = 0
j = len(arr)-1

while i != j:
    value = arr[i] + arr[j]
    if abs(minValue) > abs(value):
        minValue = value
        minX = arr[i]; minY = arr[j]
    if arr[i] + arr[j] == 0:
        break
    elif arr[i] + arr[j] < 0:
        i+=1
    elif arr[i] + arr[j] > 0:
        j-=1
print(minX, minY)
