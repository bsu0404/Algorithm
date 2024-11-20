from collections import deque
MOVE = [[0,1],[-1,0],[0,-1],[1,0]]


def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for move in MOVE:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]=="#" and not visited[nx][ny]:
                queue.append((nx,ny))



N, M = map(int, input().split())
arr  = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == "#" and not visited[i][j]:
            bfs(i,j)
            count += 1

print(count)