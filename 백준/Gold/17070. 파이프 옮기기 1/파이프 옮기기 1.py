MOVE  = [[0,-1],[-1,0],[-1,-1]] # 옆, 위, 대각선
N = int(input())
mtx = []
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)] # 가로, 세로, 대각선
dp[0][1][0] = 1
# 벽 정보
for i in range(N):
    tmp = list(map(int, input().split()))
    mtx.append(tmp)

for i in range(N):
    for j in range(N):
        if mtx[i][j] == 0:
            for k in range(3):
                x, y = i + MOVE[k][0], j + MOVE[k][1]
                if 0 <= x < N and 0 <= y < N:
                    if k == 0: # 옆인 경우
                        dp[i][j][0] += dp[x][y][0]
                        dp[i][j][0] += dp[x][y][2]
                    if k == 1: # 위인 경우
                        dp[i][j][1] += dp[x][y][1]
                        dp[i][j][1] += dp[x][y][2]
                    if k == 2 and mtx[i-1][j] == 0 and mtx[i][j-1] == 0: # 대각선인 경우
                        dp[i][j][2] += dp[x][y][0]
                        dp[i][j][2] += dp[x][y][1]
                        dp[i][j][2] += dp[x][y][2]                

print(sum(dp[N-1][N-1]))