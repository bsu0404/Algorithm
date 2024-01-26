from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N, H = map(int, input().split()) #가로, 세로, 높이

graph = [[[0] * M for _ in range(N)] for _ in range(H)]

for i in range(H): # 높이
    for j in range(N): # 세로
        row = list(map(int, input().split())) #가로줄
        graph[i][j] = row


total = M*N*H #총 토마토 수
ripe = set() #익은 토마토

for i in range(H):
    for j in range(N):
        for k in range(M):
            if(graph[i][j][k]==-1): 
                total-=1
            if(graph[i][j][k]==1):       
                ripe.add((i,j,k))


MOVE = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]


maxCount=0
def bfs() :
    visited=[[[0]*M for _ in range(N)] for _ in range(H)]
    needVisit = deque(ripe)

    while needVisit:
        global maxCount
        x,y,z = needVisit.popleft()
        count = graph[x][y][z]
        maxCount = max(count,maxCount)
        ripe.add((x,y,z))
        visited[x][y][z]=1

        for move in MOVE:
            xx, yy,zz = move
            nx, ny , nz = x + xx, y +yy, z+zz
            if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M)and (visited[nx][ny][nz] == 0) :
                if 0<graph[nx][ny][nz]<=count:
                    visited[nx][ny][nz] = 1
                    needVisit.append([nx, ny,nz])       
                if  graph[nx][ny][nz]==0:
                    graph[nx][ny][nz] = count+1
                    needVisit.append([nx, ny,nz])       


if len(ripe)==total:
    print(0)
    sys.exit()

bfs()

if(len(ripe)==total):
    print(maxCount-1)
else:
    print(-1)
