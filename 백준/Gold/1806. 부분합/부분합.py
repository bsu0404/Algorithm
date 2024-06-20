N, S = map(int, input().split())

arr = list(map(int, input().split()))
arr = [0] + arr
for i in range(1,N + 1):
    arr[i] += arr[i-1]

i = 0
j = 0
cnt = N + 2
while j < N + 1 and i <= j:
    if arr[j] - arr[i] < S:
        j += 1
    else:
        if cnt > j - i:
            cnt = j - i    
        i += 1
        
print(cnt if cnt != N + 2 else 0)