from collections import deque

N = int(input())
arr = list(map(int,input().split()))
stack = deque()
ans = []

for i in range(N):
    num = arr[i]

    while stack and stack[-1][0] <= num:
        tmp = stack.pop()
    
    ans.append(stack[-1][1] if stack else 0)
    stack.append([num, i + 1])

print(*ans)