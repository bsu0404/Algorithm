from collections import deque

# fucntion

i = 0
def traversal(node):
    global  i

    if node * 2 < maxNum : 
        traversal(node * 2)

    tree[node] = arr[i]
    i += 1

    if node * 2 + 1 < maxNum :
        traversal(node * 2 + 1)
    

#main
N = int(input())
maxNum = 2**N 
arr = list(map(int,input().split()))
tree = [0] * maxNum

traversal(1)

for i in range(N):
    tmp = tree[2**i:2**(i+1)]
    print(*tmp)
