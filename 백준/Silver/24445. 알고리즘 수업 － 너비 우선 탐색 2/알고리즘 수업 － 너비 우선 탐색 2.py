from collections import deque
import sys
input = sys.stdin.readline


def bfs(s):
    global count
    queue = deque()
    queue.append(s)


    while queue:
        node = queue.popleft()
        if visited[node] != -1:
            continue
        
        visited[node] = count
        count += 1

        for next_node in adjList[node]:
            if visited[next_node] == -1:
                queue.append(next_node)

N, M, R = map(int,input().split())
adjList = [[] for _ in range(N+1) ]
visited = [-1] * (N+1)
count = 1

for _ in range(M):
    v1,v2 = map(int,input().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)

for i in range(N+1):
    adjList[i].sort(reverse=True)

bfs(R)

for i in range(1,N+1):
    print(visited[i] if visited[i]!=-1 else 0)