import sys

N, K = map(int, input().split())
arr = list(map(int,input().split()))
ans = -sys.maxsize
sum = 0

for i in range(N):
    sum += arr[i]

    if i >= K:
        sum -= arr[i-K]

    if sum > ans and i + 1 >= K:
        ans = sum


    
print(ans)