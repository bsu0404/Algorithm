from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    queue = deque()
    queue.append([i,j,0])

    visited[i][j] = True
    while queue:
        x, y, count = queue.popleft()  

        for move in MOVE:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == '0':
                    queue.append([nx,ny,count+1])
                elif arr[nx][ny] != '1' and arr[nx][ny] != '0':
                    print("TAK")
                    print(count+1)
                    quit()
    print("NIE")


MOVE = [[0,1],[-1,0],[0,-1],[1,0]]

N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
visited = [ [False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '2':
            bfs(i,j)



