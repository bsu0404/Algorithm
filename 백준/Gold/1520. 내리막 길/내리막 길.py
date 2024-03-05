from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
MOVE = [[-1,0], [0,-1], [1,0], [0,1]] #상, 좌, 하, 우

def dfs(x, y):
    # 도착지
    if x == N-1 and y == M-1:
        return 1
    # 갔던길이면 또 안감
    if dp[x][y] != -1:
        return dp[x][y]
    # 방문처리
    dp[x][y] = 0

    # 상하좌우
    for move in MOVE:
        nx = x + move[0]
        ny = y + move[1]
        # 내리막길이면
        if 0 <= nx < N and 0 <= ny < M and mtx[nx][ny] < mtx[x][y]:
            value = dfs(nx,ny)
            dp[x][y] += value

    return dp[x][y]


count = dfs(0, 0)

print(count)
