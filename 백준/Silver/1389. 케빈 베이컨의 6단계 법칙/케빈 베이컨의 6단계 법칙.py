from collections import deque

def bfs(start):
    queue = deque()
    queue.append([start, 1])
    visited[start][start] = 0
    
    while queue:
        s, count = queue.popleft() 
        if visited[start][s] == 0:
            visited[start][s] = count
        else:
            continue

        for e in graph[s]: 
            if (visited[start][e] == 0):
                queue.append([e, count + 1])
       
# main
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [[0 for _ in range(N+1)]for _ in range(N+1)]

for _ in range(M):
    p1, p2 = map(int,input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

for i in range(1, N+1):
    bfs(i)
minV = sum(visited[1])
minI = 1
for i in range(2,N+1):
    s = sum(visited[i])
    if minV > s:
        minV = s
        minI = i
print(minI)