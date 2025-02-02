from collections import deque
MOVE = [[1,0],[0,1],[-1,0],[0,-1]]


def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1
        for xx, yy in MOVE:
            nx, ny = xx + x, yy + y
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return cnt



N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for i in range(N)]
ans = 0
maxD = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            c = bfs(i,j)
            ans += 1
            maxD = max(maxD, c)


print(ans)
print(maxD)