from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append([x,y,0])
    visited[x][y] = 0
    
    while queue:
        x, y, count = queue.popleft()


        for move in MOVE:
            nx, ny = x + move[0], y + move[1]               
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] > count + 1 and mtx[nx][ny] == "." :
                visited[nx][ny] = count + 1
                queue.append([nx,ny,count + 1])

def bfs2(x,y):
    queue = deque()
    queue.append([x,y,0])
    visited2[x][y] = 0
    
    while queue:
        x, y, time = queue.popleft()

        for move in MOVE:
            nx, ny = x + move[0], y + move[1]               

            if 0 <= nx < R and 0 <= ny < C and mtx[nx][ny] == "D":
                return time + 1

            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] > time + 1 and mtx[nx][ny] == "." and visited2[nx][ny] == -1:
                visited2[nx][ny] = time + 1
                queue.append([nx, ny, time + 1])

R, C = map(int, input().split())

mtx = [list(input()) for _ in range(R)]
visited = [[3000]*C for _ in range(R)]
visited2 = [[-1]*C for _ in range(R)]

waterList =[]
MOVE = [[1, 0], [-1 ,0], [0, 1], [0, -1]] 

for i in range(R):
    for j in range(C):
        if mtx[i][j] == "S":
            idxS = [i,j]
        elif mtx[i][j] == "*":
            waterList.append([i,j])
        

for i, j in waterList:
    bfs(i,j)
time = bfs2(idxS[0],idxS[1])

if time is None:
    print("KAKTUS")
else:
    print(time)

