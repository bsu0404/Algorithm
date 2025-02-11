from collections import deque
from itertools import combinations

MOVE = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs(i, j):
    queue = deque()
    cnt = 1
    queue.append((i,j))
    visited[i][j] = True
    isSafe = True


    while queue:
        x, y = queue.popleft()

        for nx, ny in MOVE:
            xx, yy = x + nx, y + ny

            if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy] and arr[xx][yy] == 0:
                queue.append((xx, yy))
                visited[xx][yy] = True
                cnt += 1
            if 0 <= xx < N and 0 <= yy < M and arr[xx][yy] == 2:
                isSafe = False

    if isSafe:
        return cnt
    else:
        return 0
    
# 벽을 조합마다 바이러스 침투 bfs 돌리고 => 안전구역 bfs (X) 
# 벽을 조합마다 안전구역 bfs => 바이러스 만나나면 safe x (O)

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
empty = []


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i,j))


# 새로 만들 벽의 위치 조합
combs = list(combinations(empty, 3))
maxCount = 0

for locations in combs:
    visited = list([False]*M for _ in range(N))
    cnt = 0

    for x,y in locations:
        arr[x][y] = 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 0:     
                cnt += bfs(i, j)

    for x,y in locations:
        arr[x][y] = 0
        
    maxCount = max(cnt, maxCount)


print(maxCount)
