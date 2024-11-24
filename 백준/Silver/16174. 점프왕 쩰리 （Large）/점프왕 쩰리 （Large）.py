from collections import deque
MOVE = [[1,0],[0,1]]

def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        num = arr[x][y]

        if x == N-1 and y == N-1:
            print("HaruHaru")
            exit()

        for move in MOVE:
            dx, dy = x + move[0] * num,  y + move[1] * num

            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
                queue.append((dx,dy))
                visited[dx][dy] = True

    print("Hing")



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

bfs()