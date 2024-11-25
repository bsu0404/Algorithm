from collections import deque


N = int(input())
arr = [int(input()) for _ in range(N)]

stack = deque()
j = 0
ans  = []

for i in range(1,N+1):
    
    stack.append(i)
    ans.append("+")

    while stack and stack[-1] == arr[j]:
        stack.pop()
        j += 1
        ans.append("-")
        
if stack:
    print("NO")
else:
    print(*ans,sep="\n")