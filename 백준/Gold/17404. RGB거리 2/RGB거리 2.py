import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())

cost = [list(map(int,input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
ans = INF

# r, g, b 순으로 시작을 정해두고 dp구하기
for i in range(3): 
    #  초기값: 시작 이외에는 INF (정해둔 시작 값을 사용하도록)
    dp[0][i] = cost[0][i]
    for j in range(3):
        if i == j:
            dp[0][j] = cost[0][i]
        else:
            dp[0][j] = INF
    
    # dp[x][y]: x번재 집 y번째 색상을 고른 경우 최소값
    for j in range(1,N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]
    
    for j in range(3):
        if i == j:
            continue
        else:
            ans = min(ans, dp[N-1][j])
print(ans)
    
