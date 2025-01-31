from collections import deque
from itertools import combinations

MOVE = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs(locations):
    queue = deque()
    for l in locations:
        queue.append((virus[l][0],virus[l][1],0))
        visited.add((virus[l][0],virus[l][1]))

    while queue:
        x, y, cnt = queue.popleft()

        for nx, ny in MOVE:
            xx, yy = x + nx, y + ny

            if 0 <= xx < N and 0 <= yy < N and (xx,yy) not in visited and arr[xx][yy]!= 1:
                queue.append((xx, yy, cnt + 1))
                visited.add((xx,yy))
    return cnt


N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
wallCount = 0
virus = []
ans = 50000000

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            wallCount += 1
        elif arr[i][j] == 2:
            virus.append((i, j))

nums = range(0, len(virus)) 
combs = list(combinations(nums, M))

for locations in combs:
    visited = set()
    cnt = bfs(locations)
    if N * N - wallCount == len(visited):
        ans = min(ans, cnt)
print(ans if ans != 50000000 else -1)