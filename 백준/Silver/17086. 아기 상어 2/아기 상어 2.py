from collections import deque
import queue
import sys
N, M = map(int,input().split())

arr = list(input().split() for _ in range(N))
visited = [ [0]*M for _ in range(N)]

sharks = []

# 1 의 위치 저장 => 전체 돌면서 비교 (v) -> 대각선 가능이라서 안됨

# 1의 위치에서 bfs 돌면서 거리 저장


for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            sharks.append([i, j])

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            minDist = sys.maxsize
            for shark in sharks:
                # dist = abs(i - shark[0]) + abs(j - shark[1])
                diff = abs(abs(i - shark[0]) - abs(j -shark[1]))
                dist = min( abs(i - shark[0]),abs(j - shark[1])) + diff
                minDist = min(minDist, dist)
            if minDist > ans:
                ans = minDist

print(ans)

