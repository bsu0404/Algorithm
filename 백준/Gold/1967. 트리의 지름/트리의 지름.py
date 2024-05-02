
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(index, cost):
    global maxIndex, maxCost
    visited[index] = 1
    visitArr = []

    for node in tree[index]:
        if visited[node[0]] == 0:
            visitArr.append(node)
    # 말단 노드
    if len(visitArr) == 0:  
        if maxCost < cost:
            maxCost = cost
            maxIndex = index
    # 이어진 노드로 이동
    for node in visitArr:
        visited[node[0]] = 1
        dfs(node[0], cost + node[1])


# main
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2, w = map(int, input().split())
    tree[v1].append([v2, w])
    tree[v2].append([v1, w])

visited = [0] * (N + 1)
maxCost = 0
maxIndex = -1
dfs(1,0)

maxCost = 0
visited = [0] * (N + 1)
dfs(maxIndex, 0)

print(maxCost)