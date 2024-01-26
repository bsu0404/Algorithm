from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
total = M*N #총 토마토 수
ripe = set() #익은 토마토

for i in range(N):
    for j in range(M):
        if(graph[i][j]==-1): 
            total-=1
        if(graph[i][j]==1):       
            ripe.add((i,j))


MOVE = [[-1,0],[1,0],[0,-1],[0,1]]
maxCount = 0

def bfs() :
    visited=[[0]*M for _ in range(N)]
    needVisit = deque(ripe)

    while needVisit:
        global maxCount
        x,y = needVisit.popleft()
        count = graph[x][y]
        maxCount = max(count,maxCount)
        ripe.add((x,y))
        visited[x][y]=1

        for move in MOVE:
            xx, yy = move
            nx, ny = x + xx, y +yy
            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0) :
                if 0<graph[nx][ny]<=count:
                    visited[nx][ny] = 1
                    needVisit.append([nx, ny])       
                if  graph[nx][ny]==0:
                    graph[nx][ny] = count+1
                    needVisit.append([nx, ny])       


if len(ripe)==total:
    print(0)
    sys.exit()

bfs()

if(len(ripe)==total):
    print(maxCount-1)
else:
    print(-1)
       