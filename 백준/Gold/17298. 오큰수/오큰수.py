from collections import deque

N = int(input())
arr  = list(map(int,input().split()))
ans = [-1]*N

i = N - 1
stack = deque()
stack.append(N - 1)

while i > 0: # n
    i -= 1
    while stack and arr[i] >= arr[stack[-1]]:
        stack.pop()

    if stack:
        ans[i] = arr[stack[-1]]

    stack.append(i)
    
    
print(' '.join(map(str, ans)))