n = int(input())

dp = [0, 0, 0, 1 ,0 ,1]

for i in range(6, n+1):
    if dp[i-3] == 0 and dp[i-5] == 0: 
        dp.append(0)
    elif dp[i-3] != 0 and   dp[i-5] != 0:
        dp.append(min(dp[i - 3] , dp[i - 5]) + 1) 
    elif dp[i-3] != 0:
        dp.append(dp[i - 3] + 1)
    elif dp[i-5] != 0:
        dp.append(dp[i - 5] + 1)

print(dp[n] if dp[n] != 0 else -1)