import sys
input = sys.stdin.readline

dp = [[0]*32 for _ in range(32)]

for i in range(0,32):
    for j in range(i,32):
        if i == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])