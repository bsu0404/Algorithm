a=1
b=1
c=1

dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                dp[i][j][k] = 1
            elif i < j and j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

a,b,c = map(int,input().split())

while a!=-1 or b!=-1 or c!=-1:
    if a <= 0 or b <= 0 or c <= 0:
        print("w(%d, %d, %d) = %d" %(a,b,c,1))
    elif a > 20 or b > 20 or c > 20:
        print("w(%d, %d, %d) = %d" %(a,b,c,dp[20][20][20]))
    else:
        print("w(%d, %d, %d) = %d" %(a,b,c,dp[a][b][c]))

    a,b,c = map(int,input().split())
