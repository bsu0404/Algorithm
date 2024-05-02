# fucntion

from collections import deque

ans1 = ""
ans2 = ""
ans3 = ""
def traversal(node):
    global ans1, ans3, ans2
    ans1 += chr(node + 64)

    if tree[node][0] != 0 : 
        traversal(tree[node][0])
    ans2 += chr(node + 64)
    
    if tree[node][1] != 0:
        traversal(tree[node][1])
    ans3 += chr(node + 64)
    



#main
N = int(input())

tree = [[0,0] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N):
    p, c1, c2 = input().split()
    p = ord(p)-64
    if c1 != ".":
        tree[p][0] = ord(c1)-64
    if c2 != ".":
        tree[p][1] = ord(c2)-64


traversal(1)
print(ans1)
print(ans2)
print(ans3)