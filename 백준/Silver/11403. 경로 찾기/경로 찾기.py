from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
adjMtx = [list(map(int, input().split())) for _ in range(N)]
visited = [set() for _ in range(N)]

def bfs(X):
    que = deque([X])

    while que:
        x = que.popleft()

        for i in range(N):
            if adjMtx[x][i] == 1 and i not in visited[X]:
                visited[X].add(i)
                que.append(i)

for i in range(N):
    bfs(i)

visitedMtx = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if j in visited[i]:
            visitedMtx[i][j] = 1
for x in visitedMtx:
    print(*x)