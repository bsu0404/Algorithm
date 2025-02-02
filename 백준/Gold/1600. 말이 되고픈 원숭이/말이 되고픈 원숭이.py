from collections import deque

MOVE = [[1,0],[0,1],[-1,0],[0,-1]]
HMOVE = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]
def bfs():
    visited[0][0][0] = K
    queue = deque()
    queue.append((0,0,0,0))

    while queue:
        x, y, cnt, d = queue.popleft()

        if x == N-1 and y == M-1:
            return cnt

        for move in HMOVE:
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]==0 and d + 1 <= K and visited[d+1][nx][ny] == 0 :
                visited[d+1][nx][ny] = cnt + 1
                queue.append((nx,ny, cnt + 1, d + 1))
 

        for move in MOVE:
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < N and 0 <= ny < M  and arr[nx][ny]==0 and visited[d][nx][ny] == 0:
                visited[d][nx][ny] = cnt + 1
                queue.append((nx,ny, cnt + 1, d))
    return -1



K = int(input())

M, N = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(K+1)] 

ans = bfs()
print(ans)