N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

negative,positive=[],[]
ans,maxD = 0,0

for i in range(N):
    if arr[i] < 0:
        negative.append(arr[i])
    else:
        positive.append(arr[i])


for i in range(len(positive)-1,-1,-M):
    ans += positive[i]
for i in range(0,len(negative),M):
    ans += (-negative[i]) 

if positive:
    maxD = positive[-1]
if negative:
    maxD = max(maxD,abs(negative[0]))

print(ans*2 - maxD)

