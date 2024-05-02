from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        node = queue.popleft()

        for i in range(len(tree[node])):
            if visited[tree[node][i]] == 0:
                queue.append(tree[node][i])
                visited[tree[node][i]] = node

# main
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N-1)]
tree = [[] for _ in range(N + 1)]
visited = [0] * (N+1)

# 인접 리스트
for i in range(N-1):
    n1 = arr[i][0]
    n2 = arr[i][1]

    tree[n1].append(n2)
    tree[n2].append(n1)

bfs()

print(*visited[2:],sep="\n")

