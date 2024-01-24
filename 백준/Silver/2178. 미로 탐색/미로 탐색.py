from collections import deque

MOVE = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs():
    minCount = float("inf")
    needVisit = deque()
    x,y=0,0
    visited = [[0] * M for _ in range(N)]
    needVisit.append([x, y, 0])
    visited[x][y] = 1
    
    while len(needVisit)>0:
        x, y, count = needVisit.popleft()

        if x == N-1 and y == M-1:
            minCount = min(count, minCount)

        for move in MOVE:
            xx, yy = move
            nx, ny = x + xx, y + yy           
            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0) and (graph[nx][ny]==1):
                visited[nx][ny] = 1
                needVisit.append([nx, ny, count + 1])
    print(minCount+1)

N,M = map(int,input().split())
graph =[]
for i in range(N):
    row = list(map(int, input()))
    graph.append(row)
bfs()