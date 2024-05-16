N = int(input())
arr = []
for _ in range(N):
    s = input()
    arr.append(s)
arr.sort()
cnt = [1] * N
for i in range(N):
    for j in range(i):
        l = len(arr[j])
        if arr[i][0:l]!=arr[j]:
            cnt[i] = max(cnt[j]+1, cnt[i])
print(max(cnt)) 