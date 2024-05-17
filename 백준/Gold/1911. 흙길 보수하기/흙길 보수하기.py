from math import ceil

N , L = map(int,input().split())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s,e-1])
arr.sort(key=lambda x:x[0])

ans  = 0
for i in range(N):
    s = arr[i][0]
    e = arr[i][1]
    len = e - s + 1
    cnt = ceil(len/L)
    ans += cnt
    # 다음 시작 <= 현재 끝
    if i < N - 1 and arr[i+1][0] <= s + cnt * L - 1: 
        arr[i+1][0] = s + cnt * L 
print(ans)
    
