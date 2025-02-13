def findMinDiff(l, r):
    global ansL, ansR, minDiff
    while l < r:
        diff = arr[l] + arr[r]
        

        if abs(diff) < minDiff:
            minDiff = abs(diff)
            ansL = arr[l]
            ansR = arr[r]

        if diff >  0:
            r = r - 1
        elif diff < 0:
            l = l + 1
        elif diff == 0:
            print(arr[l],arr[r])
            exit()

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

negative = []
positive = []
zeroIndex = []

for i in range(N):
    num = arr[i]
    if num < 0:
        negative.append(num)
    if num == 0:
        zeroIndex.append(i)
    if num > 0:
        positive.append(num)

minDiff = float("inf")   


ansL = -1
ansR = -1
if len(zeroIndex) >=2:
    ansL, ansR = 0, 0
elif len(zeroIndex) == 1:
    if positive and positive[0] < minDiff:
        minDiff = positive[0]
        ansL, ansR = 0 ,positive[0]
    if negative and abs(negative[0]) < minDiff:
        minDiff = abs(negative[-1])
        ansL, ansR = negative[-1], 0
else:

    findMinDiff(0, N-1)


    if len(positive) >= 2 and positive[0] + positive[1] < minDiff:
        minDiff = positive[0] + positive[1]
        ansL, ansR = positive[0] , positive[1]
    
    if len(negative) >= 2 and abs(negative[-1] + negative[-2]) < minDiff:
        minDiff = abs(negative[-2] + negative[-1])
        ansL, ansR = negative[-2] , negative[-1]
print(ansL, ansR)