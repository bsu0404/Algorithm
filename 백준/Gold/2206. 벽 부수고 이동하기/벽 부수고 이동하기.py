from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int,input().split())
disable = sys.maxsize
mtx = [list(map(int,input().strip())) for _ in range(N)]
visited = [[[ 0, 0] for _ in range(M)] for _ in range(N)] 
# [0번 부신 경우, 1번 부신 경우]
def bfs():
    needVisit = deque()  
    needVisit.append([0, 0, 0 ])
    visited[0][0] = [1,0]
    MOVE = [[1, 0], [-1 ,0], [0, 1], [0, -1]] 
    
    while needVisit:
        x, y, z = needVisit.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for xx,yy in MOVE:
            nx = x + xx           
            ny = y + yy
            
            if not (0 <= nx < N) or not (0 <= ny < M) :
                continue

            if mtx[nx][ny] == 0 and mtx[x][y] == 0 and visited[nx][ny][z] == 0: #길 => 길
                visited[nx][ny][z] = visited[x][y][z] + 1
                needVisit.append([nx,ny,z])
            elif mtx[nx][ny] == 1 and mtx[x][y] == 0 and visited[nx][ny][z] == 0 and z == 0: # 길 => 벽
                visited[nx][ny][1] = visited[x][y][z] + 1
                needVisit.append([nx,ny,1])
            elif mtx[nx][ny] == 1 and mtx[x][y] == 1: # 벽 => 벽
                continue  
            elif mtx[nx][ny] == 0 and mtx[x][y] == 1 and visited[nx][ny][z] == 0: #  벽 => 길 
                visited[nx][ny][z] = visited[x][y][z] + 1
                needVisit.append([nx,ny,z])   
              
            
minValue = bfs()
if minValue is None:
    print(-1)
else:
    print(minValue)