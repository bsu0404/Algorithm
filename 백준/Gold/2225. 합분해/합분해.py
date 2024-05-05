N, M = map(int,input().split())
dp = [[0] * (N+2) for _ in range(M)]
for i in range(N+2):
    dp[0][i] = 1
for i in range(1,M):
    for j in range(N+2):
        for k in range(j-1):
            dp[i][j] += (dp[i-1][j-k])
        dp[i][j] += 1
print(dp[M-1][N+1] % 1000000000)