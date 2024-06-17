# function 

import sys
INF = sys.maxsize
input = sys.stdin.readline


def find(i, j):
    k = prev[i][j]
    if k == -1:
        return [i]
    return find(i,k) + find(k, j)

# main

N = int(input())
M = int(input())

adjList = [[] for _ in range(N + 1)]
cost = [[INF] * (N + 1) for _ in range(N + 1)]
prev = [[-1] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adjList[s].append((e, w))
    if w < cost[s][e]:
        cost[s][e] = w

for i in range(N + 1):
    cost[i][i] = 0

for k in range(N+1):
    for i in range(N + 1):
        for j in range(N + 1):
            newCost = cost[i][k] + cost[k][j]
            if cost[i][j] > newCost:
                cost[i][j] = newCost
                prev[i][j] = k

for i in range(N+1):
    for j in range(N+1):
        if cost[i][j] >= INF:
            cost[i][j] = 0

for x in cost[1:]:
    print(*x[1:], sep=" ")

for i in range(1, N+ 1):
    for j in range(1, N + 1):
        if i == j or cost[i][j] == 0:
            print(0)
        else:
            l = find(i, j) + [j]
            print(len(l), *l)
            

