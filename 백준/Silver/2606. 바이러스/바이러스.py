from collections import deque

import sys
input = sys.stdin.readline
def bfs(i):
    global count
    count += 1
    queue = deque()
    queue.append(i)


    while queue:
        node = queue.popleft()
        visited.add(node)


        for next_node in adsList[node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)




N = int(input())
M = int(input())

visited = set()
adsList= [[] for _ in range(N + 1)]
count = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    adsList[v1].append(v2)
    adsList[v2].append(v1)

bfs(1)

print(len(visited)-1)