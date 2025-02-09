N = int(input())
H = []
stack=[]
ans = 0
for _ in range(N):
    H.append(int(input()))

for i in range(N -1 ,-1,-1):
    h = H[i]
    count = 0
    while stack and stack[-1][1] < h:
        s = stack.pop()
        count += (s[2] + 1)
        
    stack.append([i,h,count])  
    ans += count 


print(ans)