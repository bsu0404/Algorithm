N, H = map(int, input().split())
arr = [0] * (H+1)
arr2 = [0] * (H+1)

for i in range(N):
    num = int(input())
    if i % 2 == 0:
        arr[num] += 1
    else:
        arr2[num] += 1


for i in range(H - 2, -1, -1):
    arr[i] += arr[i+1]
    arr2[i] += arr2[i+1]

minH = 500001
minCount = 0

arr2 = arr2[::-1]

for i in range(H):
    tmp = arr[i + 1] + arr2[i]
    if tmp < minH:
        minH = tmp
        minCount = 1
    elif tmp == minH :
        minCount += 1

print(minH, minCount)