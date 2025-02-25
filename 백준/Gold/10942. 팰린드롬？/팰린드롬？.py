import sys
input = sys.stdin.readline

N = int(input())
str= list(map(int,input().split()))
lenStr = len(str)
dp = [[False] * (lenStr + 1) for _ in range(lenStr+1)]

for i in range(lenStr+1):
    dp[i][i] = True

for i in range(1,lenStr+1):
    for j in range(1,i):
        # 사이가 팰린드롬, 일치
        if dp[i-1][j+1] and str[i-1] == str[j-1]:
            dp[i][j] = True
        # 길이 2, 일치
        if j + 1 == i and str[i-1] == str[j-1]:
            dp[i][j] = True


M = int(input())
for i in range(M):
    s, e = map(int,input().split())
    print(1 if dp[e][s] else 0)
