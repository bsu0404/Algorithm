N, mile = map(int,input().split())
arr = []

for i in range(N):
    p,l = map(int,input().split())
    tmp = list(map(int, input().split()))
    tmp.sort(reverse=True)
    if p < l: 
        arr.append(1)
    else:
        arr.append(tmp[l-1])

arr.sort()
i = 0
cnt = 0

while i < len(arr) and arr[i] <= mile :
    mile -= arr[i]
    i += 1
    cnt += 1

print(cnt)

