N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 1000001
stack = []
ans = [-1] * N

for num in arr:
    cnt[num] += 1

for i in range(N -1 ,-1,-1):
    h = cnt[arr[i]]
    count = 0
    while stack and stack[-1][1] <= h:
        s = stack.pop()

    if stack:
        ans[i] = arr[stack[-1][0]]
    stack.append([i,h])

print(*ans,sep=" ")