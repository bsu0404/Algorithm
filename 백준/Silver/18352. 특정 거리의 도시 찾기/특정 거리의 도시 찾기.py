from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X = map(int,(input().split()))
adjList = [[] for _ in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    adjList[a].append(b)

visited = [0] * (N+1)

def bfs():
    global N,M,X,K
    queue = deque([X])
    visited[X] = 1

    while queue:
        x = queue.popleft()
        if visited[x] == K + 1:
            continue

        for move in adjList[x]:           
            if visited[move] == 0 :
                visited[move] = visited[x] + 1
                queue.append(move)
    
bfs()
existFlag = False
for i in range(1, N+1) :
    if visited[i] == K + 1 :
        print(i)
        existFlag = True

if not existFlag :
    print(-1)