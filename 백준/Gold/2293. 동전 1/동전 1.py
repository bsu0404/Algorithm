len,goal = map(int,input().split())

array = list(int(input()) for _ in range(len)) #코인 가치 배열
dp = [0]*100001

for i in range(len):
    coin = array[i] #코인의 가치
    dp[coin] = dp[coin]+1
    for j in range(1,goal+1):
        if j-coin>0:
            ref = dp[j-coin]
            dp[j] = ref + dp[j]
print(dp[goal])