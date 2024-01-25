from collections import deque

N,M = map(int,input().split())

graph = [ list(input()) for _ in range(N)]

maxCount = 0
MOVE = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(x,y) :
    visited=[[0]*M for _ in range(N)]
    needVisit = deque()
    needVisit.append([x,y,0])
    visited[x][y]=1

    while(needVisit):
        global maxCount
        x,y,count = needVisit.popleft()
        maxCount = max(count, maxCount)

        for move in MOVE:
            xx, yy = move
            nx, ny = x + xx, y +yy
            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0) and graph[nx][ny]=='L':
                visited[nx][ny] = 1
                needVisit.append([nx, ny, count + 1])


for i in range(N):
    for j in range(M):
        if graph[i][j]=='L':
            bfs(i,j)

print(maxCount)