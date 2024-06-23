# main

T = int(input())

N = int(input())
a = [0] + list(map(int, input().split()))
M = int(input())
b = [0] +list(map(int, input().split()))

# 누적합
for i in range(N):
    a[i+1] += a[i]
for i in range(M):
    b[i+1] += b[i]

dic = {}
for i in range(M + 1):
    for j in range(i):
        sum = b[i] - b[j]
        if sum not in dic:
            dic[sum] = 0
        dic[sum] += 1

ans = 0
for i in range(N + 1):
    for j in range(i):
        sum = a[i] - a[j]
        tmp = T - sum
        if tmp in dic:
            ans += dic[tmp]

print(ans)               