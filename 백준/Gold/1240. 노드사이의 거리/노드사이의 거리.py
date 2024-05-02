
# function
def dfs(index, s, e, count):
    global ans
    visited[index] = 1
    if index == e:
        ans = count
        return count
    
    for node in tree[index]:
        if visited[node[0]] == 0:
            visited[node[0]] = 1
            dfs(node[0], s, e, count + node[1])


#main

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visited = [0] * (N+1)
ans = 0

for _ in range(N-1):
    v1, v2, w = map(int, input().split())
    tree[v1].append([v2, w])
    tree[v2].append([v1, w])

for _ in range(M):
    v1, v2 = map(int, input().split())
    visited = [0] * (N+1)
    dfs(v1, v1, v2, 0)
    print(ans)
