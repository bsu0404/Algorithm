import sys
N = int(input())

house = list(map(int,input().split()))
house.sort()

sumRight, sumLeft = [0], [0]
ans,ansIndex = sys.maxsize, 0

for i in range(1, N):
    sumRight.append(sumRight[-1] + (house[i] - house[i-1])*i)
    sumLeft.append(sumLeft[-1] + (house[N-i]-house[N-i-1])*i)

for i in range(N):
    if ans > sumRight[i] + sumLeft[N - i - 1]:
        ans = sumRight[i] + sumLeft[N - i - 1]
        ansIndex = i
        
print(house[ansIndex])