import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
l = len(arr)
tree = [0]*(4*l)

def init(start, end, node):
    if start == end:
        tree[node] = [arr[start], start]
        return tree[node]
    mid = (start+end) //2
    left  = init(start, mid, node*2)
    right = init(mid + 1, end, node*2+1)
    if left[0] <= right[0]:
        tree[node] = [left[0], left[1]]
    else:
        tree[node] = [right[0], right[1]]

    return tree[node]

init(0,l-1,1)

def update(start, end, node, index):
    if index < start or index > end :
        return tree[node]
    if start == end:
        tree[node] = [arr[start], start]
        return tree[node]
    
    mid = (start+end) // 2
    left  = update(start, mid, node * 2, index)
    right = update(mid + 1, end, node*2+ 1, index)
    if left[0] <= right[0]:
        tree[node] = [left[0], left[1]]
    else:
        tree[node] = [right[0], right[1] ]

    return tree[node]


M = int(input())
for i in range(M):
    q = list(map(int, input().split()))
    if len(q) == 1: # 최소 출력
        print(tree[1][1] + 1)
    else: 
        query, index, num = q[0], q[1], q[2]
        arr[index - 1] = num
        update(0, l-1, 1, index -1)

        

