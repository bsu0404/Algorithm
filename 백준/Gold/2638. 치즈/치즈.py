from collections import deque
MOVE = [[0,1],[-1,0],[0,-1],[1,0]]


def dfs(i,j,type):
    stack = deque()
    stack.append((i,j))
    visited[i][j] = True


    while stack:
        x, y = stack.popleft()
        count = 0

        for move in MOVE:
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < N and 0 <= ny < M and (arr[nx][ny] == 0 or arr[nx][ny] == -1 )and not visited[nx][ny] and type == "air": # 공기가 공기를 만난 경우
                visited[nx][ny] = True
                arr[nx][ny] = 0 # 이전 턴에 치즈였던 부분 => 공기
                stack.append((nx,ny))

            elif 0 <= nx < N and 0 <= ny < M and (arr[nx][ny] == 1 or arr[nx][ny] == -1) and not visited[nx][ny] and type=="cheese": # 치즈가 치즈를 만난 경우
                stack.append((nx,ny))
                visited[nx][ny] = True

            elif 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] and type=="cheese": # 치즈가 공기를 만난 경우
                count += 1

        if count >= 2: # 치즈가 공기를 두군데 이상 만난 경우
            arr[x][y] = -1



N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0

while True: 
    visited = [[0] * M for _ in range(N)]
    dfs(0,0,"air") # 바깥 벽 visited true 처리 (0,0은 공기)
    cheese = 0 # 치즈 덩어리 수

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                # 바깥 벽: arr[i]==0 and visited[i][j] == true
                dfs(i,j,"cheese")
                cheese += 1
    if cheese == 0:
        break
    ans += 1

print(ans)